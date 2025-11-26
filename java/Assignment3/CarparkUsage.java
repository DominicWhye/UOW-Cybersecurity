/*
 * Module code: CSIT213
 * Assignment name: Assignment 3
 * UOW student number: 9891092
 * Full name: WHYE LI HENG DOMINIC
 * Tutorial group: T01
 */

import java.time.LocalDate;
import java.time.format.DateTimeParseException;


public class CarparkUsage {

    private final String carparkName;
    private final String zone; //zone the carpark belongs to
    private final LocalDate usageDate; //date of usage in YYYY-MM-DD
    private final double occupiedRate; //percentage of occupied lots


    public CarparkUsage(String carparkName, String zone, String usageDate, double occupiedRate)
            throws CarparkDataException {
        if (carparkName == null || zone == null || usageDate == null) {
            throw new CarparkDataException("Null value provided for carpark usage record");
        }
        this.carparkName = carparkName.trim();
        this.zone = zone.trim();
        LocalDate date;
        try {
            date = LocalDate.parse(usageDate.trim());
        } catch (DateTimeParseException ex) {
            // carparkdataexception when the date is invalid
            throw new CarparkDataException("Invalid date: " + usageDate, ex);
        }
        // Validate occupied rate range (must be within 0-100)
        if (occupiedRate < 0.0 || occupiedRate > 100.0) {
            throw new CarparkDataException("Occupied rate out of valid range: " + occupiedRate);
        }
        this.usageDate = date;
        this.occupiedRate = occupiedRate;
    }

 
    public String getName() {
        return carparkName;
    }

  
    public String getZone() {
        return zone;
    }

   
    public int getYear() {
        return usageDate.getYear();
    }

    
    public int getMonth() {
        return usageDate.getMonthValue();
    }

  
    public double getOccupiedRate() {
        return occupiedRate;
    }

   
    //two usage records are equal only if they refer to the same caprark name and usage date

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (!(obj instanceof CarparkUsage)) {
            return false;
        }
        CarparkUsage other = (CarparkUsage) obj;
        return this.carparkName.equals(other.carparkName)
                && this.usageDate.equals(other.usageDate);
    }

    @Override
    public int hashCode() {
        int result = carparkName.hashCode();
        result = 31 * result + usageDate.hashCode();
        return result;
    }

   
    @Override
    public String toString() {
        return String.format("%s %s %s %s",usageDate.toString(),carparkName,zone,occupiedRate);
    }
}
