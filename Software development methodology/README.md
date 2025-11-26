# Volunteer Management System

A web-based platform connecting Corporate Social Responsibility (CSR) representatives with Persons-in-Need (PIN) for volunteer opportunities and community service matching.

## Overview

This system facilitates connections between individuals seeking assistance and corporate volunteers looking to give back to their communities. The platform supports multiple user roles and streamlines the volunteer matching process.

## Features

### User Roles
- **User Admin:** Manage user accounts and profiles
- **Platform Manager:** Oversee categories and generate reports
- **CSR Representative:** Browse opportunities, create shortlists, and track volunteer history
- **Person-in-Need (PIN):** Create assistance requests and track past requests

### Core Functionality
- User account management with role-based access control
- Category-based volunteer opportunity organization (100+ categories)
- Request creation and history
- Shortlist management for CSR representatives
- Volunteer service history tracking
- Daily, weekly, and monthly reporting
- Real-time opportunity view and shortlist counters

## Technology Stack

- **Backend:** Python, Flask
- **Database:** SQLite3
- **Frontend:** HTML, CSS, JavaScript, Jinja2 templates
- **Architecture:** BCE (Boundary-Entity-Controller)

## Test Data

The system includes pre-populated dummy data for testing and demonstration purposes.

I'll help you create comprehensive documentation for the mock data. Here's the filled-out description:

***

### Sample Data Included

**Categories (100 volunteer opportunity types)**
- Located in: `database/mock-data/category.sql`
- Contains 100 diverse volunteer categories including Elderly Care, Food Distribution, Youth Programs, etc.
- All categories include names, descriptions, and active/inactive status flags

**User Accounts (100 distinct user accounts)**
- Located in: `database/mock-data/user.sql`
- Pre-configured test accounts for all user roles (see Default User Credentials section)
- Includes sample data for names, emails, addresses, phone numbers, and account statuses

**User Profiles (4 distinct user profiles/types)**
- Located in: `database/mock-data/userprofile.sql`
- Links users to their respective roles (User Admin, Platform Manager, CSR Rep, PIN)
- Includes profile descriptions and role assignments

**Requests (100 volunteer service requests)**
- Located in: `database/mock-data/request.sql`
- Contains requests from PIN (Person In Need) users seeking volunteer assistance
- Each request includes:
  - PIN user who created the request
  - Optional CSR Rep assigned to handle the request
  - Associated volunteer category
  - Status (0 = uncompleted, 1 = completed)
  - Request date ranging from January to July 2025
  - View count (number of times the request was viewed)
  - Shortlist count (number of times the request was saved to shortlists)
- Covers diverse scenarios: some requests are assigned to CSR Reps, others are unassigned
- Request statuses vary between completed and in-progress

**Shortlists (30 saved requests)**
- Located in: `database/mock-data/shortlist.sql`
- Represents CSR Representatives' saved/bookmarked requests for follow-up
- Each shortlist entry links a specific CSR Rep user to a request they've marked for attention
- Contains shortlists from 10 different CSR Rep users (user IDs: 3, 5, 8, 12, 15, 18, 22, 25, 30, 33)
- Each CSR Rep has shortlisted 3 different requests
- Enforces uniqueness constraint to prevent duplicate shortlisting of the same request by the same user
- Useful for testing CSR workflow features like task management and request tracking

***
