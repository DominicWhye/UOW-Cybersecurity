package Assign1;

//CSIT213
//Assignment 1
//UOW No. 9891092
//WHYE LI HENG, DOMINIC
//TUT GRP 1

public class Product{
    private String productId;
    private String prodDesc;
    private String category;
    private double price;
    private int stockQty;

public Product(String pID, String description, String cat, double pricing, int stockQ) {
    productId = pID;
    prodDesc = description;
    category = cat;
    price = pricing;
    stockQty = stockQ;
}
    public String getProductId() {return productId;}
    public String getProdDesc() {return prodDesc;}
    public String getCategory() {return category;}
    public double getPrice() {return price;}
    public int getStockQty() {return stockQty;}

    // public void reduceStock(int qty) {
    //     for (int i = 0; i<qty.length - 1; i++){

    //     }
    // }

    public void reduceStock(int qty) {
        if (qty < 0 || qty > stockQty) {
            throw new IllegalArgumentException("Invalid quantity to reduce: " + qty); //to ensure that qty is not negative and qty is not more than however much stock we have
        }
        stockQty -= qty;
    }

    // public boolean equals (Object obj){
    //     // return (id.equalsIgnoreCase(obj.id));
    //     return false;
    // }

    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Product)) return false;
        Product other = (Product) obj;
        return productId.equalsIgnoreCase(other.productId);
    }

    public String toString() {
        return String.format( "Product[id=%s, Description=%s, price=%.1f, stock=%d]", productId, prodDesc, price, stockQty); //to one decimal place as required in the test script
    }

}