/*
 * Module code: CSIT213
 * Assignment name: Assignment 2
 * UOW student number: 9891092
 * Full name: WHYE LI HENG DOMINIC
 * Tutorial group: T01
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Party {
    private String partyName;
    private String leaderName;
    private String symbol;
    private String slogan;

    
    private HashMap<String, ArrayList<Candidate>> candidatesMap;

   
    public Party(String partyName, String leaderName, String symbol, String slogan) {
        this.partyName = partyName;
        this.leaderName = leaderName;
        this.symbol = symbol;
        this.slogan = slogan;
        this.candidatesMap = new HashMap<>();
    }

    
    //Adds candidate to the party's internal map and group by constituency name
    //create new list if the list does not exist
    public void addCandidate(Candidate c) {
        if (c == null) {
            return;
        }
        String key = c.getConstituency();
        ArrayList<Candidate> list = candidatesMap.get(key);
        if (list == null) {
            list = new ArrayList<>();
            candidatesMap.put(key, list);
        }
        list.add(c);
    }

    
    //retrieves candidate by NRIC and returns first matching candidate , else return null
    public Candidate getCandidateByNric(String nric) {
        if (nric == null) {
            return null;
        }
        for (Map.Entry<String, ArrayList<Candidate>> entry : candidatesMap.entrySet()) {
            for (Candidate c : entry.getValue()) {
                if (c.getNric().equals(nric)) {
                    return c;
                }
            }
        }
        return null;
    }

    
    //print all candidates and group it by constituency
    public void listCandidates() {
        for (Map.Entry<String, ArrayList<Candidate>> entry : candidatesMap.entrySet()) {
            String constituency = entry.getKey();
            ArrayList<Candidate> list = entry.getValue();
            System.out.println("Constituency: " + constituency);
            for (Candidate c : list) {
                System.out.println("  " + c.toString());
            }
        }
    }

  
    public HashMap<String, ArrayList<Candidate>> getCandidates() {
        return candidatesMap;
    }

   
    public ArrayList<Candidate> getAllCandidates() {
        ArrayList<Candidate> result = new ArrayList<>();
        for (ArrayList<Candidate> list : candidatesMap.values()) {
            result.addAll(list);
        }
        return result;
    }

   
    public String getPartyName() {
        return partyName;
    }

  
    public String getLeaderName() {
        return leaderName;
    }

   
    public String getSymbol() {
        return symbol;
    }

   
    public String getSlogan() {
        return slogan;
    }
}