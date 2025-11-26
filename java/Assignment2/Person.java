/*
 * Module code: CSIT213
 * Assignment name: Assignment 2
 * UOW student number: 9891092
 * Full name: WHYE LI HENG DOMINIC
 * Tutorial group: T01
 */

public class Person {
    private String name;
    private String nric;
    private String gender;
    private String dateOfBirth;

    
    public Person(String name, String nric, String gender, String dateOfBirth) {
        this.name = name;
        this.nric = nric;
        this.gender = gender;
        this.dateOfBirth = dateOfBirth;
    }

  
    public String getName() {
        return name;
    }

    
    public String getNric() {
        return nric;
    }

    
    public String getGender() {
        return gender;
    }

    //Returns DOB of this person
    public String getDateOfBirth() {
        return dateOfBirth;
    }

    
    //Returns a string representation of the person
    @Override
    public String toString() {
        // return name + " (" + nric + ")";
        return String.format("%s (%s)", name, nric);

    }
}