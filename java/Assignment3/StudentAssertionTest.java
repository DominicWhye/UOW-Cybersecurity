import java.util.ArrayList;
import java.util.HashMap;

public class StudentAssertionTest {

	private static void run() {

		if (testAssertionEnabled()) {

			try {
				testCarparkDataException();
				System.out.println("CarparkDataException class test passed");
			} catch (AssertionError ex) {
				System.out.println("CarparkDataException class test failed:" + ex);
			}

			try {
				testCarparkUsage();
				System.out.println("CarparkUsage class test passed");
			} catch (AssertionError ex) {
				System.out.println("CarparkUsage class test failed:" + ex);
			}

			try {
				testZoneAnalyser();
				System.out.println("ZoneAnalyser class test passed");
			} catch (AssertionError ex) {
				System.out.println("ZoneAnalyser class test failed:" + ex);
			}
			
			try {
				testCarparkStat();
				System.out.println("CarparkStat class test passed");
			} catch (AssertionError ex) {
				System.out.println("CarparkStat class test failed:" + ex);
			}
			
			//write more test cases on your own here.....

		}

	}

	private static void testCarparkUsage() {
		try {
			CarparkUsage cu = new CarparkUsage("CP1", "ZoneA", "2025-01-25", 75.0);
			assert cu.getName().equals("CP1") : "Carpark name mismatch";
			assert cu.getZone().equals("ZoneA") : "Zone mismatch";
			assert cu.getYear() == 2025 : "Year mismatch";
			assert cu.getMonth() == 1 : "Month mismatch";
			assert cu.getOccupiedRate() == 75.0 : "Occupied rate mismatch";
		} catch (CarparkDataException e) {
			assert false : "Exception should not be thrown for valid data";
		}
		
		try {
            CarparkUsage cu = new CarparkUsage("CP6", "ZoneE", "2025-01-25", 88.5);
            String expected = "2025-01-25 CP6 ZoneE 88.5";
            assert cu.toString().equals(expected) : "toString output mismatch";
        } catch (CarparkDataException e) {
            assert false : "Exception should not be thrown in toString test";
        }
	}
	
	 public static void testCarparkStat() {
	        CarparkStat stat = new CarparkStat();
	        String filename = "valid_data.txt";
	        ArrayList<String> errors = stat.load(filename);
	        assert errors.size() == 0 : "There should be no errors in valid data";
	        assert stat.size() == 5 : "5 Usage data should be loaded";
	        
	        String output = stat.toString();
	        String expectedString = "2025-02-10 CP1 ZoneA 50.0\n"
	        		+ "2025-02-10 CP2 ZoneA 70.0\n"
	        		+ "2025-02-10 CP3 ZoneB 30.0\n"
	        		+ "2025-02-10 CP4 ZoneB 50.0\n"
	        		+ "2025-02-10 CP5 ZoneB 50.0\n";
	        
	        assert output.equals(expectedString) : "toString should include carpark details from valid_data.txt";
	        
	        
	        stat = new CarparkStat();
	        stat.load("valid_data.txt");

	        Analyser mockAnalyser = new ZoneAnalyser();
	        HashMap<String, Double> result = stat.process(mockAnalyser);

	        assert result != null : "Process should return a non-null result";
	        
	        System.out.println(result);
	        assert result.size() == 2 : "Result should contain 2 zone averages";
	        assert result.containsKey("ZoneA") : "Result should contain ZoneA";
	        assert result.containsKey("ZoneB") : "Result should contain ZoneB";

	        assert Math.abs(result.get("ZoneA") - 60.0) < 0.01 : "ZoneA value should be 60.0";
	        assert Math.abs(result.get("ZoneB") - 43.33) < 0.01 : "ZoneB value should be 43.333333333333336";	        
     }
	 
	private static void testZoneAnalyser() {
		ArrayList<CarparkUsage> data = new ArrayList<>();

		try {
			data.add(new CarparkUsage("CP1", "ZoneA", "2025-02-10", 50));
			data.add(new CarparkUsage("CP2", "ZoneA", "2025-08-01", 70));
			data.add(new CarparkUsage("CP3", "ZoneB", "2025-08-01", 30));
			data.add(new CarparkUsage("CP4", "ZoneB", "2025-08-01", 50));
			data.add(new CarparkUsage("CP5", "ZoneB", "2025-08-01", 40));
		} catch (Exception ex) {
			System.out.println(ex);
		}

		ZoneAnalyser analyser = new ZoneAnalyser();
		HashMap<String, Double> result = analyser.analyse(data);

		assert result.containsKey("ZoneA") : "ZoneA should be in result";
		assert result.containsKey("ZoneB") : "ZoneB should be in result";

		assert Math.abs(result.get("ZoneA") - 60.0) < 0.001 : "ZoneA average should be 60.0";
		assert Math.abs(result.get("ZoneB") - 40.0) < 0.001 : "ZoneB average should be 40.0";
	}

	private static void testCarparkDataException() {

		String message = "Invalid carpark data format";
		CarparkDataException ex = new CarparkDataException(message);
		assert ex.getMessage().equals(message) : "Message constructor failed";

		message = "Error parsing carpark data";
		Throwable cause = new NumberFormatException("Invalid number");
		CarparkDataException ex2 = new CarparkDataException(message, cause);

		assert ex2.getMessage().equals(message) : "Message in second constructor failed";
		assert ex2.getCause().equals(cause) : "Cause in second constructor failed";

		try {
			throw new CarparkDataException(message, cause);
		} catch (CarparkDataException e) {
			assert e.getMessage().equals(message) : "Message in second constructor failed";
		} catch (Exception e) {
			throw new AssertionError("CarparkDataException throw failed");
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
