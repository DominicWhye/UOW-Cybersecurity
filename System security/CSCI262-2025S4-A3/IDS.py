import random
import os
import sys
from datetime import datetime, timedelta
import math


class Event:
    def __init__(self, name, event_type, min_val, max_val, weight):
        self.name = name
        self.type = event_type  # 'C' or 'D'
        self.min = float(min_val) if min_val != '' else 0.0
        
        self.max = float(max_val) if max_val != '' else float('inf')
        self.weight = int(weight)


class EventStats:
    def __init__(self, name, mean, std_dev):
        self.name = name
        self.mean = float(mean)
        self.std_dev = float(std_dev)


class EventSystem:
    def __init__(self):
        self.events = []
        self.stats = {}
        # usings baseline_stats to hold mean and standard deviation
        self.baseline_stats = {}
        self.log_data = []

    # ------------- INITIAL INPUT -------------

    def load_initial_input(self, events_file, stats_file):
        """Load and parse Events.txt and Stats.txt files"""
        print("Loading initial input files")

        # Load Events.txt
        try:
            with open(events_file, 'r') as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]

            num_events = int(lines[0])
            print(f"Number of events (declared): {num_events}")

            for i in range(1, num_events + 1):
                if i >= len(lines):
                    print("WARNING: Fewer event lines than declared in Events.txt")
                    break

                parts = lines[i].split(':')
                if len(parts) >= 5:
                    name = parts[0]
                    event_type = parts[1]
                    min_val = parts[2]
                    max_val = parts[3]
                    weight = parts[4]

                    event = Event(name, event_type, min_val, max_val, weight)
                    self.events.append(event)
                    print(
                        f"Loaded event: {name} ({event_type}) "
                        f"min:{min_val} max:{max_val} weight:{weight}"
                    )

            if len(self.events) != num_events:
                print(
                    f"WARNING: Parsed {len(self.events)} events but header says {num_events}"
                )

        except Exception as e:
            print(f"Error loading Events.txt: {e}")
            return False

        # Load Stats.txt
        try:
            with open(stats_file, 'r') as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]

            num_stats = int(lines[0])
            print(f"Number of statistics (declared): {num_stats}")

            for i in range(1, num_stats + 1):
                if i >= len(lines):
                    print("WARNING: Fewer stats lines than declared in Stats.txt")
                    break

                parts = lines[i].split(':')
                if len(parts) >= 3:
                    name = parts[0]
                    mean = parts[1]
                    std_dev = parts[2]

                    stats = EventStats(name, mean, std_dev)
                    self.stats[name] = stats
                    print(f"Loaded stats: {name} mean:{mean} std_dev:{std_dev}")

            if len(self.stats) != num_stats:
                print(
                    f"WARNING: Parsed {len(self.stats)} stats but header says {num_stats}"
                )

        except Exception as e:
            print(f"Error loading Stats.txt: {e}")
            return False

        # checking for inconsistencies
        return self._check_consistencies()

    def _check_consistencies(self):
        """Check for inconsistencies between Events.txt and Stats.txt"""
        print("\nChecking for inconsistencies...")

        event_names = {event.name for event in self.events}
        stat_names = set(self.stats.keys())

        # Missing events in Stats.txt
        missing_in_stats = event_names - stat_names
        if missing_in_stats:
            print(f"WARNING: Events missing in Stats.txt: {missing_in_stats}")

        # Stats for events that don't exist in Events.txt
        missing_in_events = stat_names - event_names
        if missing_in_events:
            print(f"WARNING: Stats missing in Events.txt: {missing_in_events}")

        # Valid event types and min/max logic
        for event in self.events:
            if event.type not in ['C', 'D']:
                print(f"WARNING: Invalid event type '{event.type}' for event '{event.name}'")

            # Check min <= max if max is not infinite
            if event.max != float('inf') and event.min > event.max:
                print(
                    f"WARNING: For event '{event.name}', min ({event.min}) "
                    f"is greater than max ({event.max})"
                )

        # Check stats values against event ranges
        for name, stats in self.stats.items():
            
            if stats.std_dev < 0:
                print(
                    f"WARNING: Negative standard deviation for event '{name}': "
                    f"{stats.std_dev}"
                )
            # Mean vs min/max 
            ev = next((e for e in self.events if e.name == name), None)
            if ev:
                if stats.mean < ev.min or stats.mean > ev.max:
                    print(
                        f"WARNING: Mean {stats.mean} for event '{name}' lies "
                        f"outside [{ev.min}, {ev.max}]"
                    )

        if not missing_in_stats and not missing_in_events:
            print("No major name mismatches found between Events.txt and Stats.txt")

        return True

    # ------------- ACTIVITY ENGINE -------------

    def _normal_distribution_value(self, mean, std_dev):
        """Generate a value from normal distribution using Box-Muller transform"""
        u1 = random.random()
        u2 = random.random()
        z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
        return mean + z0 * std_dev

    def generate_events(self, days):
        """Activity Engine: Generate events for specified number of days"""
        print(f"\nGenerating events for {days} days...")
        self.log_data = []

        for day in range(1, days + 1):
            if day == 1 or day == days or day % max(1, days // 10) == 0:
                print(f"Generating day {day}/{days}...")

            # Generate daily totals for each event
            daily_totals = {}
            for event in self.events:
                if event.name in self.stats:
                    daily_total = self._generate_daily_total(event)
                    daily_totals[event.name] = daily_total

                    # For discrete events generate individual occurrences
                    if event.type == 'D':
                        for _ in range(int(daily_total)):
                            timestamp = self._generate_timestamp(day)
                            self.log_data.append({
                                'day': day,
                                'event_name': event.name,
                                'value': 1,
                                'timestamp': timestamp
                            })
                    else:  # Continuous events
                        timestamp = self._generate_timestamp(day)
                        self.log_data.append({
                            'day': day,
                            'event_name': event.name,
                            'value': daily_total,
                            'timestamp': timestamp
                        })

        # to save to log file
        self._save_log_file()
        print(f"Event generation completed. Generated {len(self.log_data)} event records.")

    def _generate_daily_total(self, event):
        """Generate daily total for a specific event"""
        stats = self.stats[event.name]

        if event.type == 'D':  # Discrete events
            
            value = self._normal_distribution_value(stats.mean, stats.std_dev)
            value = round(value)
          
            value = max(event.min, value)
            value = min(event.max, value)
            return int(value)
        else:  # Continuous events
            value = self._normal_distribution_value(stats.mean, stats.std_dev)
            value = max(event.min, value)
            value = min(event.max, value)
            return round(value, 2)

    def _generate_timestamp(self, day):
        """Generate a random timestamp for a given day"""
        base_date = datetime(2025, 1, 1) + timedelta(days=day - 1)
        random_hour = random.randint(0, 23)
        random_minute = random.randint(0, 59)
        random_second = random.randint(0, 59)

        timestamp = base_date.replace(
            hour=random_hour,
            minute=random_minute,
            second=random_second
        )
        return timestamp.strftime("%Y-%m-%d %H:%M:%S")

    def _save_log_file(self):
        """Save generated events to log file"""
        if not self.log_data:
            print("No log data to save.")
            return

        with open('event_logs.csv', 'w') as f:
            f.write('day,event_name,value,timestamp\n')
            for record in self.log_data:
                f.write(
                    f"{record['day']},{record['event_name']},"
                    f"{record['value']},{record['timestamp']}\n"
                )
        print("Log file saved as 'event_logs.csv'")

    # ------------- ANALYSIS ENGINE -------------

    def analyze_baseline(self):
        """Analysis Engine: Analyze baseline data from log files"""
        print("\nStarting analysis phase...")

        if not self.log_data:
            # This is to try to load from the log file
            try:
                self.log_data = []
                with open('event_logs.csv', 'r') as f:
                    lines = f.readlines()
                
                for line in lines[1:]:
                    values = line.strip().split(',')
                    record = {
                        'day': int(values[0]),
                        'event_name': values[1],
                        'value': float(values[2]),
                        'timestamp': values[3]
                    }
                    self.log_data.append(record)
                print("Loaded existing log data from 'event_logs.csv'")
            except Exception:
                print("No log data available. Please generate events first.")
                return False

        # Compute daily totals for each event
        daily_totals = {}
        for record in self.log_data:
            day = record['day']
            event_name = record['event_name']
            value = record['value']

            if day not in daily_totals:
                daily_totals[day] = {}

            if event_name not in daily_totals[day]:
                daily_totals[day][event_name] = 0

            daily_totals[day][event_name] += value

        # Save daily total to  separate file
        self._save_daily_totals(daily_totals)

        # Calculate statistics for each event
        event_stats = {}
        for event in self.events:
            event_name = event.name
            daily_values = []
            for day in sorted(daily_totals.keys()):
                if event_name in daily_totals[day]:
                    daily_values.append(daily_totals[day][event_name])
                else:
                    daily_values.append(0)

            if daily_values:
                mean = sum(daily_values) / len(daily_values)
                variance = sum((x - mean) ** 2 for x in daily_values) / len(daily_values)
                std_dev = math.sqrt(variance)

                event_stats[event_name] = {
                    'mean': round(mean, 2),
                    'std_dev': round(std_dev, 2)
                }

                print(f"{event_name}: mean={mean:.2f}, std_dev={std_dev:.2f}")

        self.baseline_stats = event_stats

        # to save baseline statistics
        self._save_baseline_stats()
        print("Analysis completed. Baseline statistics calculated and saved.")
        return True

    def _save_daily_totals(self, daily_totals):
        """Save daily totals for each event to a file"""
        with open('daily_totals.csv', 'w') as f:
            f.write('day,event_name,total\n')
            for day in sorted(daily_totals.keys()):
                for event_name, total in daily_totals[day].items():
                    f.write(f"{day},{event_name},{total}\n")
        print("Daily totals saved as 'daily_totals.csv'")

    def _save_baseline_stats(self):
        """Save baseline statistics to file"""
        if not self.baseline_stats:
            print("No baseline statistics to save.")
            return

        with open('baseline_stats.csv', 'w') as f:
            f.write('event_name,mean,std_dev\n')
            for event_name, stats in self.baseline_stats.items():
                f.write(f"{event_name},{stats['mean']},{stats['std_dev']}\n")
        print("Baseline statistics saved as 'baseline_stats.csv'")

    # ------------- ALERT ENGINE -------------

    def detect_anomalies(self, new_stats_file, days):
        """Alert Engine: Detect anomalies using new statistics"""
        print(f"\nStarting anomaly detection with {new_stats_file} for {days} days...")

        # to load new statistics
        new_stats = self._load_stats_file(new_stats_file)
        if not new_stats:
            print("Failed to load new statistics file.")
            return

        if not self.baseline_stats:
            print("Error: Baseline stats not available. Run baseline first.")
            return

        # to generate events with new statistics
        original_stats = self.stats.copy()
        self.stats = new_stats

        print("Generating new event data...")
        self.generate_events(days)

        # to calculate threshold where it is 2 * sum of weights
        total_weights = sum(event.weight for event in self.events)
        threshold = 2 * total_weights
        print(f"Anomaly threshold: {threshold}")

        # compute daily totals for anomaly detection
        daily_totals = {}
        for record in self.log_data:
            day = record['day']
            event_name = record['event_name']
            value = record['value']

            if day not in daily_totals:
                daily_totals[day] = {}

            if event_name not in daily_totals[day]:
                daily_totals[day][event_name] = 0

            daily_totals[day][event_name] += value

        # detect anomalies per day
        print("\nDaily Anomaly Report:")
        print("Day | Threshold | Anomaly Counter | Status")
        print("-" * 50)

        for day in sorted(daily_totals.keys()):
            anomaly_counter = self._calculate_anomaly_counter(daily_totals[day])
            status = "FLAGGED" if anomaly_counter >= threshold else "okay"
            print(f"{day:3} | {threshold:9.2f} | {anomaly_counter:15.2f} | {status}")

        # restore the original stats
        self.stats = original_stats

    def _load_stats_file(self, stats_file):
        """Load statistics from file"""
        try:
            with open(stats_file, 'r') as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]

            num_stats = int(lines[0])
            stats = {}

            for i in range(1, num_stats + 1):
                if i >= len(lines):
                    print("WARNING: fewer lines than declared in new stats file")
                    break

                parts = lines[i].split(':')
                if len(parts) >= 3:
                    name = parts[0]
                    mean = parts[1]
                    std_dev = parts[2]

                    stats[name] = EventStats(name, mean, std_dev)
                    print(f"Loaded new stats: {name} mean:{mean} std_dev:{std_dev}")

            if len(stats) != num_stats:
                print(
                    f"WARNING: Parsed {len(stats)} stats but header says {num_stats} "
                    f"in new stats file"
                )

            return stats

        except Exception as e:
            print(f"Error loading statistics file: {e}")
            return None

    def _calculate_anomaly_counter(self, daily_totals):
        """Calculate anomaly counter for a day"""
        anomaly_counter = 0

        for event in self.events:
            event_name = event.name

            if event_name in self.baseline_stats and event_name in daily_totals:
                baseline = self.baseline_stats[event_name]
                daily_value = daily_totals[event_name]

                # to calculate standard deviations from mean
                if baseline['std_dev'] > 0:
                    deviations = abs(daily_value - baseline['mean']) / baseline['std_dev']
                else:
                    # if there is no variation then treat identical as 0 deviations
                    deviations = 0

                # apply weight
                weighted_deviation = deviations * event.weight
                anomaly_counter += weighted_deviation

        return anomaly_counter


def interactive_mode():
    """Interactive mode for user input"""
    print("=" * 60)
    print("Email System Event Modeler & Intrusion Detection System")
    print("=" * 60)

    system = EventSystem()

    # to get input files
    print("\nPlease provide the required files:")

    events_file = input("Enter path to Events.txt file (default: Events.txt): ").strip()
    if not events_file:
        events_file = "Events.txt"

    stats_file = input("Enter path to Stats.txt file (default: Stats.txt): ").strip()
    if not stats_file:
        stats_file = "Stats.txt"

    # to check if files exist
    if not os.path.exists(events_file):
        print(f"Error: Events file '{events_file}' not found!")
        return

    if not os.path.exists(stats_file):
        print(f"Error: Stats file '{stats_file}' not found!")
        return

    # get the number of days
    try:
        days = int(input("Enter number of days to generate events for (default: 30): ").strip() or "30")
    except ValueError:
        print("Invalid input. Using default value: 30 days")
        days = 30

    # Phase 1
    print("\n" + "=" * 50)
    print("PHASE 1: INITIAL INPUT")
    print("=" * 50)

    if not system.load_initial_input(events_file, stats_file):
        print("Failed to load initial input files.")
        return

    # Phase 2
    print("\n" + "=" * 50)
    print("PHASE 2: ACTIVITY ENGINE")
    print("=" * 50)

    system.generate_events(days)

    # Phase 3
    print("\n" + "=" * 50)
    print("PHASE 3: ANALYSIS ENGINE")
    print("=" * 50)

    system.analyze_baseline()

    # Phase 4
    print("\n" + "=" * 50)
    print("PHASE 4: ALERT ENGINE - INTERACTIVE MODE")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("1. Load new statistics and detect anomalies")
        print("2. View current baseline statistics")
        print("3. Regenerate events with current statistics")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            new_stats_file = input("Enter path to new statistics file: ").strip()
            if not os.path.exists(new_stats_file):
                print("File not found!")
                continue

            try:
                days_input = input("Enter number of days to analyze (default: 30): ").strip()
                days_count = int(days_input) if days_input else 30
                system.detect_anomalies(new_stats_file, days_count)
            except ValueError:
                print("Invalid number of days! Using default: 30")
                system.detect_anomalies(new_stats_file, 30)

        elif choice == '2':
            print("\nCurrent Baseline Statistics:")
            print("-" * 40)
            for event_name, stats in system.baseline_stats.items():
                print(f"{event_name}: mean={stats['mean']}, std_dev={stats['std_dev']}")

        elif choice == '3':
            try:
                days_input = input("Enter number of days to regenerate (default: 30): ").strip()
                days_count = int(days_input) if days_input else 30
                system.generate_events(days_count)
                system.analyze_baseline()
            except ValueError:
                print("Invalid number of days! Using default: 30")
                system.generate_events(30)
                system.analyze_baseline()

        elif choice == '4':
            print("Thank you for using the Email IDS. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    """Main program function"""

    if len(sys.argv) == 4:
        events_file = sys.argv[1]
        stats_file = sys.argv[2]
        days = int(sys.argv[3])

        
        if not os.path.exists(events_file):
            print(f"Error: Events file '{events_file}' not found!")
            sys.exit(1)

        if not os.path.exists(stats_file):
            print(f"Error: Stats file '{stats_file}' not found!")
            sys.exit(1)

        system = EventSystem()

        # Phase 1
        if not system.load_initial_input(events_file, stats_file):
            print("Failed to load initial input files.")
            sys.exit(1)

        # Phase 2
        system.generate_events(days)

        # Phase 3
        system.analyze_baseline()

        # Phase 4
        print("\n" + "=" * 60)
        print("ALERT ENGINE - Interactive Mode")
        print("=" * 60)

        while True:
            print("\nOptions:")
            print("1. Load new statistics and detect anomalies")
            print("2. Quit")

            choice = input("Enter your choice (1-2): ").strip()

            if choice == '1':
                new_stats_file = input("Enter path to new statistics file: ").strip()
                if not os.path.exists(new_stats_file):
                    print("File not found!")
                    continue

                days_input = input("Enter number of days to analyze: ").strip()
                try:
                    days_count = int(days_input)
                    system.detect_anomalies(new_stats_file, days_count)
                except ValueError:
                    print("Invalid number of days!")

            elif choice == '2':
                print("Thank you for using the Email IDS. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")
    else:
        interactive_mode()


if __name__ == "__main__":
    main()