import java.util.*;

public class StudentAssertionTest {

	public static void testPerson() {
		// Create a Person object
		Person person = new Person("Jane Doe", "S9876543Z", "Female", "1985-12-05");

		// Assertions to test getter methods
		assert person.getName().equals("Jane Doe") : "Name mismatch";
		assert person.getNric().equals("S9876543Z") : "NRIC mismatch";
		assert person.getGender().equals("Female") : "Gender mismatch";
		assert person.getDateOfBirth().equals("1985-12-05") : "Date of birth mismatch";

		// Assertion to test toString method
		String expectedToString = "Jane Doe (S9876543Z)";
		assert person.toString().equals(expectedToString) : "toString output mismatch";

		System.out.println("All assertions passed for Person class.");

	}

	public static void testCandidate() {
		Candidate candidate = new Candidate("John Tan", "S1234567D", "Male", "1970-01-01", "Future Party",
				"Marine Parade", "GRC");

		// Assertions to test getter methods
		assert candidate.getPartyName().equals("Future Party") : "Party name mismatch";
		assert candidate.getConstituency().equals("Marine Parade") : "Constituency mismatch";
		assert candidate.getConstituencyType().equals("GRC") : "Constituency type mismatch";

		// Test static methods
		assert Candidate.getMaxGRCCandidates() == 3 : "Default max GRC candidates should be 3";
		Candidate.setMaxGRCCandidates(5);
		assert Candidate.getMaxGRCCandidates() == 5 : "Updated max GRC candidates should be 5";

		// Test toString output contains expected values
		String output = candidate.toString();
		assert output.contains("Future Party") : "toString missing party name";
		assert output.contains("Marine Parade") : "toString missing constituency";
		assert output.contains("GRC") : "toString missing constituency type";

		System.out.println("All assertions passed for Candidate class.");
	}

	public static void testParty() {

		Party party = new Party("Vision Party", "Lee Wei", "Star", "Progress for All");

		// Assertions for basic attributes
		assert party.getPartyName().equals("Vision Party") : "Party name mismatch";

		// Create Candidate objects
		Candidate.setMaxGRCCandidates(3);
		Candidate c1 = new Candidate("Candidate 1", "S1111111A", "Male", "1975-06-15", "Vision Party", "Tampines",
				"GRC");
		Candidate c2 = new Candidate("Candidate 2", "S2222222A", "Female", "1978-09-25", "Vision Party", "Tampines",
				"GRC");
		Candidate c3 = new Candidate("Candidate 3", "S3333333A", "Male", "1980-04-14", "Vision Party", "Tampines",
				"GRC");

		Candidate c4 = new Candidate("Candidate 4", "S4444444B", "Male", "1980-03-22", "Vision Party", "Hougang",
				"SMC");

		// Add candidates to the party
		party.addCandidate(c1);
		party.addCandidate(c2);
		party.addCandidate(c3);
		party.addCandidate(c4);

		// Assertions for candidate addition
		assert party.getAllCandidates().size() == 4 : "Candidate count mismatch";
		assert party.getCandidateByNric("S1111111A").equals(c1) : "Candidate retrieval by NRIC failed";
		assert party.getCandidateByNric("S2222222A").equals(c2) : "Candidate retrieval by NRIC failed";
		assert party.getCandidateByNric("S3333333A").equals(c3) : "Candidate retrieval by NRIC failed";
		assert party.getCandidateByNric("S4444444B").equals(c4) : "Candidate retrieval by NRIC failed";
		assert party.getCandidateByNric("S0000000Z") == null : "Non-existent candidate should return null";

		// Assertions for internal data structure
		assert party.getCandidates().containsKey("Hougang") : "Hougang key missing in candidates map";
		assert party.getCandidates().containsKey("Tampines") : "Tampines key missing in candidates map";
		assert party.getCandidates().get("Hougang").size() == 1 : "Hougang Candidate list size mismatch";
		assert party.getCandidates().get("Tampines").size() == 3 : "Tampines Candidate list size mismatch";

		System.out.println("All assertions passed for Party class.");
	}

	public static void testElectionCommision() {
		ElectionCommission ec = new ElectionCommission();

		// Create two parties
		Party party1 = new Party("Progressive Alliance", "Tan Mei", "Star", "Forward Together");
		Party party2 = new Party("Unity Front", "Lee Kai", "Dove", "United We Stand");

		ec.addParty(party1);
		ec.addParty(party2);

		ArrayList<Party> parties = ec.getParties();
		assert parties.size() == 2 : "Party size mismatch";

		// Add 3 GRC candidates for each party in Tampines
		ec.addCandidateToParty("Progressive Alliance",
				new Candidate("Alice", "S1111111A", "Female", "1980-01-01", "Progressive Alliance", "Tampines", "GRC"));
		ec.addCandidateToParty("Progressive Alliance",
				new Candidate("Bob", "S2222222B", "Male", "1982-02-02", "Progressive Alliance", "Tampines", "GRC"));
		ec.addCandidateToParty("Progressive Alliance",
				new Candidate("Charlie", "S3333333C", "Male", "1984-03-03", "Progressive Alliance", "Tampines", "GRC"));

		ec.addCandidateToParty("Unity Front",
				new Candidate("Diana", "S4444444D", "Female", "1986-04-04", "Unity Front", "Tampines", "GRC"));
		ec.addCandidateToParty("Unity Front",
				new Candidate("Ethan", "S5555555E", "Male", "1988-05-05", "Unity Front", "Tampines", "GRC"));
		ec.addCandidateToParty("Unity Front",
				new Candidate("Fiona", "S6666666F", "Female", "1990-06-06", "Unity Front", "Tampines", "GRC"));

		// Add SMC candidate for party1 and party2 in Hougang
		ec.addCandidateToParty("Progressive Alliance",
				new Candidate("Grace", "S7777777G", "Female", "1992-07-07", "Progressive Alliance", "Hougang", "SMC"));
		ec.addCandidateToParty("Unity Front",
				new Candidate("Helen", "S8888888G", "Female", "1993-05-17", "Unity Front", "Hougang", "SMC"));

		ArrayList<String> candidatesTamp = ec.getCandidatesNameByConstituency("Tampines");
		ArrayList<String> dataTamp = new ArrayList<String>();
		dataTamp.add("Alice");
		dataTamp.add("Bob");
		dataTamp.add("Charlie");
		dataTamp.add("Diana");
		dataTamp.add("Ethan");
		dataTamp.add("Fiona");
		assert compareTwoArrayList(candidatesTamp, dataTamp) : "Candidates name mismatch in Tampines";

		ArrayList<String> candidatesHG = ec.getCandidatesNameByConstituency("Hougang");
		ArrayList<String> dataHG = new ArrayList<String>();
		dataHG.add("Grace");
		dataHG.add("Helen");
		assert compareTwoArrayList(candidatesHG, dataHG) : "Candidates name mismatch in Hougang";

		ArrayList<String> candidatePA = ec.getCandidatesNameByParty("Progressive Alliance");
		ArrayList<String> dataPA = new ArrayList<String>();
		dataPA.add("Alice");
		dataPA.add("Bob");
		dataPA.add("Charlie");
		dataPA.add("Grace");
		assert compareTwoArrayList(candidatePA, dataPA) : "Candidates name mismatch in Progressive Alliance";

		ArrayList<String> candidateUF = ec.getCandidatesNameByParty("Unity Front");
		ArrayList<String> dataUF = new ArrayList<String>();
		dataUF.add("Diana");
		dataUF.add("Ethan");
		dataUF.add("Fiona");
		dataUF.add("Helen");
		assert compareTwoArrayList(candidateUF, dataUF) : "Candidates name mismatch in Progressive Alliance";

		ArrayList<String> candidateAll = ec.getAllCandidatesName();
		ArrayList<String> dataAll = new ArrayList<String>();
		dataAll.addAll(dataTamp);
		dataAll.addAll(dataHG);
		assert compareTwoArrayList(candidateAll, dataAll) : "Candidates name mismatch in election";

		//add in more error test cases.....
		
		System.out.println("All assertions passed for ElectionCommission class.");
	}

	private static void run() {

		if (testAssertionEnabled()) {
			try {
				testPerson();
			} catch (AssertionError ex) {
				System.out.println("Person class test failed:" + ex);
			}

			try {
				testCandidate();
			} catch (AssertionError ex) {
				System.out.println("Candidate class test failed:" + ex);
			}

			try {
				testParty();
			} catch (AssertionError ex) {
				System.out.println("Party class test failed:" + ex);
			}

			try {
				testElectionCommision();
			} catch (AssertionError ex) {
				System.out.println("ElectionCommision class test failed:" + ex);
			}

		}
	}

	private static boolean compareTwoArrayList(ArrayList<String> als1, ArrayList<String> als2) {
		Set<String> set1 = new HashSet<>();
		set1.addAll(als1);
		Set<String> set2 = new HashSet<>();
		set2.addAll(als2);
		return set1.equals(set2);
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
