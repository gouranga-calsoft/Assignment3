#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>
#include <algorithm>
#include <stdexcept>

using namespace std;

// Class to store one inventory record
class Inventory {
public:
    string ip;
    string os;
    string memory;
    string cpu;
    string disk;

    // Convert "16GB" -> 16
    int getMemoryValue() const {
        string num = memory.substr(0, memory.find("GB"));
        return stoi(num);
    }

    // Convert "3.8Ghz" -> 3.8
    double getCpuValue() const {
        string num = cpu.substr(0, cpu.find("Ghz"));
        return stod(num);
    }

    // Print inventory details
    void print() const {
        cout << "IP     : " << ip << endl;
        cout << "OS     : " << os << endl;
        cout << "Memory : " << memory << endl;
        cout << "CPU    : " << cpu << endl;
        cout << "Disk   : " << disk << endl;
        cout << "-----------------------------------" << endl;
    }
};

// Class to manage all inventory records
class InventoryManager {
private:
    vector<Inventory> inventories;

    // Extract a value using regex
    string extractValue(const string& line, const regex& pattern) {
        smatch match;
        if (regex_search(line, match, pattern)) {
            return match[1];
        }
        return "";
    }

public:
    // Load inventory data from JSON file
    void loadFromFile(const string& filename) {
        ifstream file(filename);

        if (!file.is_open()) {
            throw runtime_error("Unable to open file: " + filename);
        }

        string line;
        Inventory current;
        bool insideRecord = false;

        // Regex patterns
        regex ipPattern("\"ip\"\\s*:\\s*\"([^\"]+)\"");
        regex osPattern("\"os\"\\s*:\\s*\"([^\"]+)\"");
        regex memoryPattern("\"memory\"\\s*:\\s*\"([^\"]+)\"");
        regex cpuPattern("\"cpu\"\\s*:\\s*\"([^\"]+)\"");
        regex diskPattern("\"disk\"\\s*:\\s*\"([^\"]+)\"");

        while (getline(file, line)) {

            // Start of a new inventory record
            if (line.find("{") != string::npos &&
                line.find("\"ip\"") == string::npos &&
                !insideRecord) {
                current = Inventory();
                insideRecord = true;
            }

            // Extract fields
            string value;

            value = extractValue(line, ipPattern);
            if (!value.empty()) current.ip = value;

            value = extractValue(line, osPattern);
            if (!value.empty()) current.os = value;

            value = extractValue(line, memoryPattern);
            if (!value.empty()) current.memory = value;

            value = extractValue(line, cpuPattern);
            if (!value.empty()) current.cpu = value;

            value = extractValue(line, diskPattern);
            if (!value.empty()) current.disk = value;

            // End of current record
            if (insideRecord &&
                line.find("}") != string::npos &&
                !current.ip.empty()) {

                inventories.push_back(current);
                insideRecord = false;
            }
        }

        file.close();
    }

    // Filter based on criterion
    void filter(const string& criterion) {
        if (criterion == "Memory") {
            if (inventories.empty()) return;

            Inventory maxInv = inventories[0];

            for (size_t i = 1; i < inventories.size(); i++) {
                if (inventories[i].getMemoryValue() >
                    maxInv.getMemoryValue()) {
                    maxInv = inventories[i];
                }
            }

            cout << "Server with Maximum Memory:\n";
            maxInv.print();
        }
        else if (criterion == "CPU") {
            if (inventories.empty()) return;

            Inventory maxInv = inventories[0];

            for (size_t i = 1; i < inventories.size(); i++) {
                if (inventories[i].getCpuValue() >
                    maxInv.getCpuValue()) {
                    maxInv = inventories[i];
                }
            }

            cout << "Server with Maximum CPU:\n";
            maxInv.print();
        }
        else if (criterion == "Linux" || criterion == "Windows") {
            cout << "Servers with OS = " << criterion << ":\n";

            bool found = false;

            for (size_t i = 0; i < inventories.size(); i++) {
                if (inventories[i].os == criterion) {
                    inventories[i].print();
                    found = true;
                }
            }

            if (!found) {
                cout << "No matching records found.\n";
            }
        }
        else {
            throw invalid_argument(
                "Invalid filter criterion. "
                "Use Memory, CPU, Linux, or Windows."
            );
        }
    }
};

// Main function
int main(int argc, char* argv[]) {
    try {
        // Check if criterion is provided
        if (argc < 2) {
            throw invalid_argument("Filter criterion is missing.");
        }

        string criterion = argv[1];

        InventoryManager manager;

        // Load data from inventory.json
        manager.loadFromFile("inventory.json");

        // Apply filter
        manager.filter(criterion);
    }
    catch (exception& e) {
        cerr << "Error: " << e.what() << endl;
        return 1;
    }

    return 0;
}