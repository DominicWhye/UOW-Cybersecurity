package Assign1;

//CSIT213
//Assignment 1
//UOW No. 9891092
//WHYE LI HENG, DOMINIC
//TUT GRP 1

public class StudentAssertionTest {

	public static void testCustomer() {
		
		// Test 1: Constructor and Getters
		Customer customer1 = new Customer("C001", "Alice", "alice@example.com");

		assert customer1.getId().equals("C001") : "ID mismatch";
		assert customer1.getName().equals("Alice") : "Name mismatch";
		assert customer1.getEmail().equals("alice@example.com") : "Email mismatch";

		// Test 2: equals() method
		Customer customer2 = new Customer("C001", "Alice", "alice@example.com");
		Customer customer3 = new Customer("C002", "Bob", "bob@example.com");
		assert customer1.equals(customer2) : "Customers with same ID should be equal";

		// Test 3: toString() method
		String expectedString = "Customer[id=C001, name=Alice, email=alice@example.com]";
		assert customer1.toString().equals(expectedString) : "toString output mismatch";

		//add in more test cases on your own....
         // Test 4: equals is case-insensitive
        Customer c4 = new Customer("c001", "Alice", "alice@example.com");
        assert customer1.equals(c4) : "equals should ignore case in IDs";

        // Test 5: reflexive property
        assert customer1.equals(customer1) : "object should equal itself";
		
		System.out.println("All Customer assertions passed.");
	}
	
	public static void testProduct() {
        Product product = new Product("P001", "Laptop", "Electronics", 1500.0, 10);

        // Test getters
        assert product.getProductId().equals("P001") : "Product ID mismatch";
        assert product.getProdDesc().equals("Laptop") : "Product description mismatch";
        assert product.getCategory().equals("Electronics") : "Category mismatch";
        assert product.getPrice() == 1500.0 : "Price mismatch";
        assert product.getStockQty() == 10 : "Stock quantity mismatch";

        // Test reduceStock
        product.reduceStock(3);
        assert product.getStockQty() == 7 : "Stock reduction failed";

        // Test equals
        Product sameProduct = new Product("P001", "Laptop", "Electronics", 1500.0, 7);
        Product differentProduct = new Product("P002", "Tablet", "Electronics", 800.0, 5);
        assert product.equals(sameProduct) : "Products with same ID should be equal";

        // Test toString
        String expected = "Product[id=P001, Description=Laptop, price=1500.0, stock=7]";
        assert product.toString().equals(expected) : "toString output mismatch";

		//add in more test cases on your own....

         // Test equals different type
        assert !product.equals("P001") : "equals should return false for non-Product";

        // Test multiple reduceStock calls
        product.reduceStock(2);
        assert product.getStockQty() == 5 : "reduceStock multiple times failed";
		
        System.out.println("All Product assertions passed.");
        
    }   
	
	public static void testOrder() {
        Customer customer = new Customer("C001", "Alice", "alice@example.com");
        Product product = new Product("P001", "Laptop", "Electronics", 1500.0, 10);
        Order order = new Order("O001", customer, product, 2, "2025-06-28");

        // Test getters
        assert order.getOrderId().equals("O001") : "Order ID mismatch";
        assert order.getCustomer().equals(customer) : "Customer mismatch";
        assert order.getProduct().equals(product) : "Product mismatch";
        assert order.getQuantity() == 2 : "Quantity mismatch";
        assert order.getOrderDate().equals("2025-06-28") : "Order date mismatch";

        // Test equals
        Order sameOrder = new Order("O001", customer, product, 2, "2025-06-28");
        Order differentOrder = new Order("O002", customer, product, 2, "2025-06-28");
        assert order.equals(sameOrder) : "Orders with same ID should be equal";

        // Test toString
        String expected = "Order[id=O001, product=Laptop, quantity=2, date=2025-06-28]";
        assert order.toString().equals(expected) : "toString output mismatch";

		//add in more test cases on your own....

         // Test reflexive
        assert order.equals(order) : "equals should be reflexive";

        // Test equals null and different type
        assert !order.equals(null) : "equals should return false for null";
        assert !order.equals("ORD1") : "equals should return false for non-Order";
		
		
        System.out.println("All Order assertions passed.");
    }
	
	
	public static void testECommerceManager() {
        ECommerceManager manager = new ECommerceManager("TechStore");

        // Create customers
        Customer c1 = new Customer("C001", "Alice", "alice@example.com");
        Customer c2 = new Customer("C002", "Bob", "bob@example.com");

        // Add customers
        assert manager.addCustomer(c1) : "Failed to add customer Alice";
        assert manager.addCustomer(c2) : "Failed to add customer Bob";

        // Create products
        Product p1 = new Product("P001", "Laptop", "Electronics", 1500.0, 5);
        Product p2 = new Product("P002", "Tablet", "Electronics", 800.0, 10);
        Product p3 = new Product("P003", "Book", "Books", 20.0, 50);

        // Add products
        assert manager.addProduct(p1) : "Failed to add product Laptop";
        assert manager.addProduct(p2) : "Failed to add product Tablet";
        assert manager.addProduct(p3) : "Failed to add product Book";

        // Place orders
        assert manager.placeOrder("C001", "P001", 2) : "Failed to place order for Laptop";
        assert manager.placeOrder("C002", "P002", 1) : "Failed to place order for Tablet";

        // Cancel order
        assert manager.cancelOrder("ORD1") : "Failed to cancel order ORD1";

        // Search by category
        Product[] electronics = manager.searchProductsByCategory("Electronics");
        assert electronics.length == 2 : "Electronics category search failed";

        Product[] books = manager.searchProductsByCategory("Books");
        assert books.length == 1 : "Books category search failed";

        // toString check
        String output = manager.toString();
        assert output.contains("=== Customers ===") : "Missing customers section";
        assert output.contains("=== Orders ===") : "Missing orders section";

		//add in more test cases on your own....

         // Verify next order ID increments
        assert manager.placeOrder("C002", "P003", 5) : "Failed to place third order";
        // Should generate ORD3
        assert manager.cancelOrder("ORD3") : "Failed to cancel order ORD3";
		
        System.out.println("All ECommerceManager assertions passed.");
	}
	
	private static void run() {
		
		if(testAssertionEnabled()) {
			try {
				testCustomer();
			}catch(AssertionError ex) {
				System.out.println("Customer test failed:"+ex);
			}
			
			try {
				testProduct();
			}catch(AssertionError ex) {
				System.out.println("Product test failed:"+ex);
			}
			
			try {
				testOrder();
			}catch(AssertionError ex) {
				System.out.println("Order test failed:"+ex);
			}
			
			try {
				testECommerceManager();
			}catch(AssertionError ex) {
				System.out.println("ECommerceManager test failed:"+ex);
			}
		}
	}
	
	private static boolean testAssertionEnabled() {
		boolean assertionsEnabled = false;
        assert assertionsEnabled = true; // Intentional side effect

        if (assertionsEnabled) {
            System.out.println("Assertions are enabled.");
            return true;
        } else {
            System.out.println("Assertions are NOT enabled. Use -ea to enable them.");
            return false;
        }
	}
	
	public static void main(String[] args) {
		run();
	}

}
