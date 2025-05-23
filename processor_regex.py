import re
def classify_with_regex(log_message):
    regex_patterns = {
        r"User User\d+ logged (in|out).": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action"
    }
    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
    return None  # Default case if no pattern matches


if __name__ == "__main__":
    print(classify_with_regex("User User123 logged in."))
    print(classify_with_regex("User User456 logged out."))
    print(classify_with_regex("Backup started at 2023-10-01 12:00:00."))
    print(classify_with_regex("Backup completed successfully."))
    print(classify_with_regex("System updated to version 2.0."))
    print(classify_with_regex("File report.pdf uploaded successfully by user User123."))
    print(classify_with_regex("Disk cleanup completed successfully."))
    print(classify_with_regex("System reboot initiated by user Admin."))
    print(classify_with_regex("Account with ID 789 created by Admin."))
    print(classify_with_regex("Unknown log message."))