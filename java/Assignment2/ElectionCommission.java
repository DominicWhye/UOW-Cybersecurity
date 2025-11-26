/*
 * Module code: CSIT213
 * Assignment name: Assignment 2
 * UOW student number: 9891092
 * Full name: WHYE LI HENG DOMINIC
 * Tutorial group: T01
 */

import java.util.ArrayList;

public class ElectionCommission {
    
    private ArrayList<Party> parties;

   
    public ElectionCommission() {
        this.parties = new ArrayList<>();
    }

    
    //Adds a new party to the commission
    public void addParty(Party p) {
        if (p == null) {
            return;
        }
        String name = p.getPartyName();
        //this is to ensure no duplicate
        for (Party existing : parties) {
            if (existing.getPartyName().equals(name)) {
                return; 
            }
        }
        parties.add(p);
    }

    // Adds a candidate to a specified party.
    public void addCandidateToParty(String partyName, Candidate c) {
        if (partyName == null || c == null) {
            return;
        }
        Party target = null;
        for (Party p : parties) {
            if (p.getPartyName().equals(partyName)) {
                target = p;
                break;
            }
        }
        if (target == null) {
            
            return;
        }
        
        if (!c.getPartyName().equals(partyName)) {
           
        }
        String constituency = c.getConstituency();
        String type = c.getConstituencyType();
        
        if (type.equals("GRC")) {
            int count = 0;
            //Count existing GRC candidates for this party in the given constituency
            ArrayList<Candidate> list = target.getCandidates().get(constituency);
            if (list != null) {
                for (Candidate existingCandidate : list) {
                    if (existingCandidate.getConstituencyType().equals("GRC")) {
                        count++;
                    }
                }
            }
            if (count >= Candidate.getMaxGRCCandidates()) {
                
                return;
            }
        }
        target.addCandidate(c);
    }

    
    public ArrayList<Party> getParties() {
        return parties;
    }

   
    //Retrieves the names of all candidates in a specified party
    public ArrayList<String> getCandidatesNameByParty(String partyName) {
        ArrayList<String> names = new ArrayList<>();
        if (partyName == null) {
            return names;
        }
        for (Party p : parties) {
            if (p.getPartyName().equals(partyName)) {
                for (Candidate c : p.getAllCandidates()) {
                    names.add(c.getName());
                }
                break;
            }
        }
        return names;
    }

    
    //retrieves the name of all candidates contesting in a specific constituency across all parties
    public ArrayList<String> getCandidatesNameByConstituency(String constituency) {
        ArrayList<String> names = new ArrayList<>();
        if (constituency == null) {
            return names;
        }
        for (Party p : parties) {
            ArrayList<Candidate> list = p.getCandidates().get(constituency);
            if (list != null) {
                for (Candidate c : list) {
                    names.add(c.getName());
                }
            }
        }
        return names;
    }

  //retrieves all candidates from all parties
    public ArrayList<String> getAllCandidatesName() {
        ArrayList<String> names = new ArrayList<>();
        for (Party p : parties) {
            for (Candidate c : p.getAllCandidates()) {
                names.add(c.getName());
            }
        }
        return names;
    }
}