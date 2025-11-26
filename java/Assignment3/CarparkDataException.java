/*
 * Module code: CSIT213
 * Assignment name: Assignment 3
 * UOW student number: 9891092
 * Full name: WHYE LI HENG DOMINIC
 * Tutorial group: T01
 */


public class CarparkDataException extends Exception {

    //handles carpark data errors by sending detail message
    public CarparkDataException(String message) {
        super(message);
    }

    public CarparkDataException(String message, Throwable cause) {
        super(message, cause);
    }
}
