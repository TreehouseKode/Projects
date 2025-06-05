#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

//DEFINITIONS FOR SHELL BUILTINS
int mash_cd(char **args);
int mash_help(char **args);
int mash_exit(char **args);

char *builtin_str[] = {
    "cd"
    "help"
    "exit"
};

int (*builtin_func[]) (char **) = {
    &mash_cd,
    &mash_help,
    &mash_exit
};

#define MASH_RL_BUFSIZE 1024

char *mash_read_line(void) {
    int bufsize = MASH_RL_BUFSIZE;
    int position = 0;
    char *buffer = malloc(sizeof(char) * bufsize);
    int c;//EOF is an int, not a char!

    if (!buffer) {
        fprintf(stderr, "mash: allocation error\n");
        exit(EXIT_FAILURE);
    }
    while (1) {
        //read a character
        c = getchar();//could simplify with getline() but this is more interesting

        //if we hit EOF, replace with null char and return
        if (c == EOF || c == '\n'){
            buffer[position] = '\0';
            return buffer;
        } else {
            buffer[position] = c;
        }
        position++;

        //if we exceed buffer, reallocate more space
        if  (position >= bufsize) {
            bufsize += MASH_RL_BUFSIZE;
            buffer = realloc(buffer, bufsize);
            if (!buffer || bufsize >= 4096) {
                fprintf(stderr, "mash: allocation err2\n");
                exit(EXIT_FAILURE);
            }
        }
    }
}

#define MASH_TOKN_BUFSIZE 64 //max arg length
#define MASH_TOKN_DELIM " \t\r\n\a"

char **mash_split_line(char *line) {//TO DO add support for quotes and backslash escaping
    int bufsize = MASH_TOKN_BUFSIZE;
    int position = 0;
    char **tokens = malloc(bufsize * sizeof(char*));
    char *token;

    if (!tokens) {
        fprintf(stderr, "mash: allocation error3\n");
        exit(EXIT_FAILURE);
    }

    token = strtok(line, MASH_TOKN_DELIM);//break the args to tokens for easier parsing
    while (token != NULL) {
        tokens[position] = token;
        position++;
        if (position >= bufsize) {
            bufsize += MASH_TOKN_BUFSIZE;
            tokens = realloc(tokens, bufsize * sizeof(char*));
            if (!tokens) {
                fprintf(stderr, "mash: allocation error4\n");
                exit(EXIT_FAILURE);
            }
        }
        token = strtok(NULL, MASH_TOKN_DELIM);
    }
    tokens[position] = NULL;
    return tokens;
}

int mash_launch(char **args){
    pid_t pid;
    pid_t wpid;
    int status;

    pid = fork();
    if (pid == 0) {//this is the child process
        if (execvp(args[0], args) == -1) {
            perror("mash: child process");
        } exit(EXIT_FAILURE);
    } else if (pid < 0){
        perror("mash: error forking");
    } else {//parent process
        do {
            wpid = waitpid(pid, &status, WUNTRACED);
        } while (!WIFEXITED(status) && !WIFSIGNALED(status));
    }

    return 1;
}



void mash_loop(void){
    char *line;
    char **args;
    int  status;

    do {
        printf("~*> ");
        line = mash_read_line();
        args = mash_split_line(line);
        status = mash_execute(args);//fork -> child exec() -> waitpid()

        free(line);
        free(args);
    } while (status);
}

int main(int argc, char **argv){
    //load config files

    //run command loop
    mash_loop();

    //shutdown and cleanup


    return EXIT_SUCCESS;
}
