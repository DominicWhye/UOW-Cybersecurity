package Assign1;

//CSIT213
//Assignment 1
//UOW No. 9891092
//WHYE LI HENG, DOMINIC
//TUT GRP 1

public class Customer{
    private String id;
    private String name;
    private String email;

    public Customer(String CustId , String CustName , String CustEmail){
        id = CustId;
        name = CustName;
        email = CustEmail;
    }

    public String getId() {return id;}
    public String getName() {return name;}
    public String getEmail() {return email;}

    // public boolean equals (Object obj){
    //     // return (id.equalsIgnoreCase(obj.id));
    //     return false;
    // }

    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Customer)) return false;
        Customer other = (Customer) obj;
        return id.equalsIgnoreCase(other.id);
    }

   
    public String toString() {
        return String.format("Customer[id=%s, name=%s, email=%s]",id, name, email);
}

   
    // public String toString() {
    //     return String.format("Customer[id=%s, name=%s, email=%s]", id,name,email);
    // }
}