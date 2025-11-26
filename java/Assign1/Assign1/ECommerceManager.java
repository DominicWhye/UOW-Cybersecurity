package Assign1;

//CSIT213
//Assignment 1
//UOW No. 9891092
//WHYE LI HENG, DOMINIC
//TUT GRP 1

import java.time.LocalDate;
import java.util.Arrays;

public class ECommerceManager {

    private String storeName;
    private Customer[] customers;
    private Product[] products;
    private Order[] orders;
    private int customerCount;
    private int productCount;
    private int orderCount;
    private final int maxItemsPerOrder = 10;
    private int nextOrderSequence = 1;


public ECommerceManager(String sName) {
    sName = storeName;
    this.customers = new Customer[100];
    this.products = new Product[100];
    this.orders = new Order[100];
    this.customerCount = 0;
    this.productCount = 0;
    this.orderCount = 0;
}

 /*
     * Adds a new customer if not already present.
     * return true if added, false if duplicate or array full.
    */
    
public boolean addCustomer(Customer c) {
    if (customerCount >= customers.length) return false;
    for (int i = 0; i < customerCount; i++) {
        if (customers[i].equals(c)) return false;
    }
    customers[customerCount++] = c;
    return true;
}

public boolean addProduct(Product p) {
    if (productCount >= products.length) return false;
    for (int i = 0; i < productCount; i++) {
        if (products[i].equals(p)) return false;
    }
    products[productCount++] = p;
    return true;
}

public Customer getCustomer(String custId) {
    for (int i = 0; i < customerCount; i++) {
        if (customers[i].getId().equalsIgnoreCase(custId)) {
            return customers[i];
        }
    }
    return null;
}

public Product getProduct(String prodId) {
    for (int i = 0; i < productCount; i++) {
        if (products[i].getProductId().equalsIgnoreCase(prodId)) {
            return products[i];
        }
    }
    return null;
}

public Product[] getAllProduct() {
    return Arrays.copyOf(products, productCount);
}

public boolean placeOrder(String custId, String prodId, int quantity) {
    Customer c = getCustomer(custId);
    Product p = getProduct(prodId);
    if (c == null || p == null || quantity <= 0 || quantity > maxItemsPerOrder || p.getStockQty() < quantity || orderCount >= orders.length) {
        return false;
    }
    String orderId = "ORD" + nextOrderSequence++;
    Order o = new Order(orderId, c, p, quantity, LocalDate.now().toString());
    orders[orderCount++] = o;
    p.reduceStock(quantity);
    return true;
}

public boolean cancelOrder(String orderId) {
    for (int i = 0; i < orderCount; i++) {
        if (orders[i].getOrderId().equalsIgnoreCase(orderId)) {
            for (int j = i; j < orderCount - 1; j++) {
                orders[j] = orders[j + 1];
            }
            orders[--orderCount] = null;
            return true;
        }
    }
    return false;
}

public Product[] searchProductsByCategory(String category) {
    Product[] temp = new Product[productCount];
    int count = 0;
    for (int i = 0; i < productCount; i++) {
        if (products[i].getCategory().equalsIgnoreCase(category)) {
            temp[count++] = products[i];
        }
    }
    return Arrays.copyOf(temp, count);
}

  
public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("=== Customers ===\n");
    for (int i = 0; i < customerCount; i++) {
        sb.append(customers[i]).append("\n");
    }
    sb.append("=== Products ===\n");
    for (int i = 0; i < productCount; i++) {
        sb.append(products[i]).append("\n");
    }
    sb.append("=== Orders ===\n");
    for (int i = 0; i < orderCount; i++) {
        sb.append(orders[i]).append("\n");
    }
    return sb.toString();
}

    
// public String toString() {
//     return String.format("%s ", storeName);
// }


}
