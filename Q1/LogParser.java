import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class LogParser {

    // Valid log types accepted from user input
    private static final Set<String> VALID_TYPES = Set.of(
            "error",
            "warning",
            "info",
            "debug"
    );

    public static void main(String[] args) {
        try {
            // ------------------------------------------------------------
            // 1. Validate required parameter: file path
            // ------------------------------------------------------------
            if (args.length < 1) {
                throw new IllegalArgumentException(
                        "Usage: java LogParser <filePath> [numberOfLines] [logTypes]"
                );
            }

            // Required argument
            String filePath = args[0];

            // Optional arguments with default values
            int numberOfLines = 10;      // default
            String logTypesArg = "error"; // default

            // ------------------------------------------------------------
            // 2. Read optional numberOfLines
            // ------------------------------------------------------------
            if (args.length >= 2) {
                numberOfLines = Integer.parseInt(args[1]);

                if (numberOfLines <= 0) {
                    throw new IllegalArgumentException(
                            "Number of lines must be greater than 0."
                    );
                }
            }

            // ------------------------------------------------------------
            // 3. Read optional log types
            // ------------------------------------------------------------
            if (args.length >= 3) {
                logTypesArg = args[2];
            }

            // ------------------------------------------------------------
            // 4. Parse and validate log types
            // ------------------------------------------------------------
            Set<String> selectedTypes = parseAndValidateLogTypes(logTypesArg);

            // ------------------------------------------------------------
            // 5. Validate file path
            // ------------------------------------------------------------
            Path path = Paths.get(filePath);

            if (!Files.exists(path) || !Files.isRegularFile(path)) {
                throw new IllegalArgumentException(
                        "Invalid file path: " + filePath
                );
            }

            // ------------------------------------------------------------
            // 6. Read all lines from the file
            // ------------------------------------------------------------
            List<String> allLines = Files.readAllLines(path);

            // ------------------------------------------------------------
            // 7. Traverse from end to start to get most recent logs
            // ------------------------------------------------------------
            List<String> result = new ArrayList<>();

            for (int i = allLines.size() - 1; i >= 0; i--) {
                String line = allLines.get(i).trim();

                // Skip empty lines
                if (line.isEmpty()) {
                    continue;
                }

                // Check whether the line matches selected log types
                if (matchesSelectedType(line, selectedTypes)) {
                    result.add(line);

                    // Stop once enough matching logs are found
                    if (result.size() == numberOfLines) {
                        break;
                    }
                }
            }

            // ------------------------------------------------------------
            // 8. Print results
            // ------------------------------------------------------------
            if (result.isEmpty()) {
                System.out.println("No matching log entries found.");
            } else {
                for (String log : result) {
                    System.out.println(log);
                }
            }

        } catch (NumberFormatException e) {
            System.err.println("Invalid number format for numberOfLines.");
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    /**
     * Parses and validates comma-separated log types.
     * Example input: "error,warning"
     */
    private static Set<String> parseAndValidateLogTypes(String logTypesArg) {
        Set<String> selectedTypes = new HashSet<>();

        String[] types = logTypesArg.split(",");

        for (String type : types) {
            String normalizedType = type.trim().toLowerCase();

            if (!VALID_TYPES.contains(normalizedType)) {
                throw new IllegalArgumentException(
                        "Invalid log type: " + normalizedType
                );
            }

            selectedTypes.add(normalizedType);
        }

        return selectedTypes;
    }

    /**
     * Checks if a log line starts with one of the selected types.
     *
     * User types:
     *   error   -> [ERROR]
     *   warning -> [WARNING]
     *   info    -> [INFO]
     *   debug   -> [DEBUG]
     */
    private static boolean matchesSelectedType(
            String line,
            Set<String> selectedTypes
    ) {
        for (String type : selectedTypes) {
            String prefix = "[" + type.toUpperCase() + "]";

            if (line.startsWith(prefix)) {
                return true;
            }
        }

        return false;
    }
}