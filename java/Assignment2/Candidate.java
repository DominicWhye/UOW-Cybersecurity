/*
 * Module code: CSIT213
 * Assignment name: Assignment 2
 * UOW student number: 9891092
 * Full name: WHYE LI HENG DOMINIC
 * Tutorial group: T01
 */

public class Candidate extends Person {
    private String partyName;
    private String constituency;
    private String constituencyType;
    
    private static int MAX_GRC_CANDIDATES = 3;

   
    public Candidate(String name, String nric, String gender, String dateOfBirth,
                     String partyName, String constituency, String constituencyType) {
        super(name, nric, gender, dateOfBirth);
        this.partyName = partyName;
        this.constituency = constituency;
        this.constituencyType = constituencyType;
    }

    
    public String getPartyName() {
        return partyName;
    }

   
    public String getConstituency() {
        return constituency;
    }

    //returns type of constituency (either SMC OR GRC)
    public String getConstituencyType() {
        return constituencyType;
    }

    
    //Retrieves current max number of candidates allowed per party in GRC
    public static int getMaxGRCCandidates() {
        return MAX_GRC_CANDIDATES;
    }

    
    //Sets max number of candidates allowed in GRC
    public static void setMaxGRCCandidates(int n) {
        MAX_GRC_CANDIDATES = n;
    }

    
    @Override
    public String toString() {
        // return super.toString() + " | Party: " + partyName + ", Constituency: " +
        //        constituency + ", Type: " + constituencyType;
        return String.format("%s | Party: %s, Constituency: %s, Type: %s",
                         super.toString(), partyName, constituency, constituencyType);
    }
}