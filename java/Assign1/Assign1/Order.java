package Assign1;

//CSIT213
//Assignment 1
//UOW No. 9891092
//WHYE LI HENG, DOMINIC
//TUT GRP 1

public class Order {
    private String orderId;
    private Customer customer;
    private Product product;
    private int quantity;
    private String orderDate;


     public Order(String oId, Customer cust, Product prod, int qty, String oDate) {
        orderId = oId;
        customer = cust;
        product = prod;
        quantity = qty;
        orderDate = oDate;
    }

    public String getOrderId(){return orderId;}
    

    public Customer getCustomer() {
        return customer;
    }

    public Product getProduct() {
        return product;
    }

    // public Customer getCustomer{
    //     for (int i = 0; i<customer.length; i++){
        
    //     return customer[i];
    // }

    // }

    // public Product getProduct(){
    // }

    public int getQuantity(){return quantity;}

    public String getOrderDate(){return orderDate;}

    // public boolean equals(Object obj){
    //     return false;
    // }

    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Order)) return false;
        Order other = (Order) obj;
        return orderId.equalsIgnoreCase(other.orderId);
    }

    public String toString(){
        return String.format("Order[id=%s, product=%s, quantity=%d, date=%s]", orderId, product.getProdDesc(), quantity, orderDate);
    }
    
}