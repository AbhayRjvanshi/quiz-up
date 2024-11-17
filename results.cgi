#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 50

// Display results for the user
void display_results(char *username) {
    char filename[MAX_LEN + 10];
    sprintf(filename, "%s_results.txt", username);  // Create the filename based on username

    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Content-Type: text/html\n\n");
        printf("<html><body><h3>No results found for user: %s</h3></body></html>", username);
        return;
    }

    printf("Content-Type: text/html\n\n");
    printf("<html><body>");
    printf("<h3>Quiz Results for %s:</h3>", username);

    char line[100];
    while (fgets(line, sizeof(line), file)) {
        printf("<p>%s</p>", line);  // Output each line (result) from the file
    }

    printf("</body></html>");

    fclose(file);
}

int main() {
    // Read input (Environment Variables) to get the username
    char *query = getenv("QUERY_STRING");
    if (query == NULL) {
        printf("Content-Type: text/plain\n\n");
        printf("No input provided.\n");
        return 1;
    }

    // Parse input (e.g., username=John)
    char username[MAX_LEN];
    sscanf(query, "username=%s", username);

    display_results(username);

    return 0;
}
