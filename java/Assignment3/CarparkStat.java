/*
 * Module code: CSIT213
 * Assignment name: Assignment 3
 * UOW student number: 9891092
 * Full name: WHYE LI HENG DOMINIC
 * Tutorial group: T01
 */


import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;


public class CarparkStat {


    private final ArrayList<CarparkUsage> usageData;

    private final ArrayList<String> error;


    public CarparkStat() {
        usageData = new ArrayList<>();
        error = new ArrayList<>();
    }

    
    public ArrayList<String> load(String filename) {
        error.clear();
        usageData.clear();

        BufferedReader reader = null;
        try {
            File file = new File(filename);
           
            if (!file.exists()) {
                file = new File(System.getProperty("user.dir"), filename);
            }
            if (file.exists()) {
                reader = new BufferedReader(new FileReader(file));
            } else {
                
                java.io.InputStream in = CarparkStat.class.getClassLoader().getResourceAsStream(filename);
                if (in != null) {
                    reader = new BufferedReader(new java.io.InputStreamReader(in));
                } else {
                    // Couldn't locate file at all; record error and return.
                    error.add("Error reading file: " + filename);
                    return new ArrayList<>(error);
                }
            }

            String line;
            while ((line = reader.readLine()) != null) {
                String trimmed = line.trim();
                if (trimmed.isEmpty()) {
                    continue;
                }
                String[] parts = trimmed.split(",");
                if (parts.length != 4) {
                    // record as error if wrong number of fields
                    error.add(trimmed);
                    continue;
                }
                //extract and trim individual fields.
                String dateStr = parts[0].trim();
                String name    = parts[1].trim();
                String zone    = parts[2].trim();
                String rateStr = parts[3].trim();
                double rate;
                try {
                    rate = Double.parseDouble(rateStr);
                } catch (NumberFormatException ex) {
                    // rate not numeric
                    error.add(trimmed);
                    continue;
                }
                try {
                    CarparkUsage record = new CarparkUsage(name, zone, dateStr, rate);
                    //skip duplicates of same name and date
                    if (!usageData.contains(record)) {
                        usageData.add(record);
                    }
                } catch (CarparkDataException ex) {
                    //invalid date or rate range
                    error.add(trimmed);
                }
            }
        } catch (IOException ex) {
            // record error if its unable to read file
            error.add("Error reading file: " + filename);
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException ignore) {
                    //ignore silently
                }
            }
        }
        return new ArrayList<>(error);
    }

    //returns the number of valid usage records that was loaded
    public int size() {
        return usageData.size();
    }

   
    public HashMap<String, Double> process(Analyser analyser) {
        if (analyser == null) {
            return null;
        }
        // Pass a copy to prevent modification of the internal list.
        return analyser.analyse(new ArrayList<>(usageData));
    }

    
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (CarparkUsage record : usageData) {
            sb.append(record.toString()).append("\n");
        }
        return sb.toString();
    }
}
