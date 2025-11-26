/*
 * Module code: CSIT213
 * Assignment name: Assignment 3
 * UOW student number: 9891092
 * Full name: WHYE LI HENG DOMINIC
 * Tutorial group: T01
 */

import java.util.ArrayList;
import java.util.HashMap;


public class ZoneAnalyser implements Analyser {

    
    @Override
    public HashMap<String, Double> analyse(ArrayList<CarparkUsage> data) {
        HashMap<String, Double> totals = new HashMap<>();
        HashMap<String, Integer> counts = new HashMap<>();
        if (data == null) {
            return new HashMap<>();
        }
        for (CarparkUsage record : data) {
            if (record == null) {
                continue;
            }
            String zone = record.getZone();
            double rate = record.getOccupiedRate();
            totals.put(zone, totals.getOrDefault(zone, 0.0) + rate);
            counts.put(zone, counts.getOrDefault(zone, 0) + 1);
        }
        HashMap<String, Double> averages = new HashMap<>();
        for (String zone : totals.keySet()) {
            double total = totals.get(zone);
            int count = counts.get(zone);
            if (count >= 0) {
                double avg = total / count;
                averages.put(zone, avg);
            }
        }
        return averages;
    }
}
