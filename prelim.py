option = 0
reports = []
report_id = 1
status_count = {
    "For Review": 0,
    "Completed": 0,
    "On Progress": 0
}
status_set = ("On Progress", "For Review", "Completed", "Rejected", "Needs Revision")   
while not option == 5:
    print("===STUDENT INCIDENT REPORT MANAGEMENT SYSTEM===")
    print("1. Submit a new report")
    print("2. Review all submitted reports")
    print("3. Update report status")
    print("4. Count report by status")
    print("5. Exit")
    option = int(input("Enter your choice: "))

    if option == 1:
        status = ""
        report = {
            "report_id": None,
            "reporter_name": None,
            "incident_type": None,
            "priority_level": None,
            "description": None,
            "is_evidence_attached": None,
            "current_status": None
        }
        print("===SUBMIT NEW REPORT===")
        reporter_name = input("Enter reporter name: ")

        incident_set = ("lost id", "room issue", "lab equipment damage", "bullying")
        incident_type = input("Enter incident type (lost id / room issue / lab equipment damage / bullying): ").lower()
        if not incident_type in incident_set:
            status = "Rejected"
            print("\nInvalid incident type. Report rejected.\n")
            reports.append(report)
            break

        priority_set= ("low", "medium", "high")
        priority_level = input("Enter priority (low / medium / high): ").strip().lower()
        if not priority_level in priority_set:
            print("\nInvalid priority level. Report rejected\n")
            reports.append(report)
            break
            
        description = input("Enter incident description: ").strip().lower()
        if len(description) < 50:
            status = "Needs Revision"


        is_evidence_attached = input("Is there evidence attached? (yes/no): ").strip().lower() == "yes"


        if priority_level == "high" and is_evidence_attached:
            status = "For Review"
        else:
            status = "On Progress"

        report["report_id"] = report_id
        report["reporter_name"] = reporter_name
        report["incident_type"] = incident_type
        report["priority_level"] = priority_level
        report["description"] = description
        report["is_evidence_attached"] = is_evidence_attached
        report["current_status"] = status
        status_count[status] += 1

        print("Report submitted successfully.")
        print(f"Assigned Report ID: {report_id}")
        print(f"Current Status: {status}")
        reports.append(report)
        report_id += 1

    elif option == 2:
        print("==ALL SUBMITTED REPORTS===")
        for report in reports:
            for key in report:
                print(f"{key}: {report[key]}")
            print("")
    elif option == 3:
        report_id = -1
        print("===UPDATE REPORT STATUS===")
        for report in reports:
            for key in report:
                print(f"{key}: {report[key]}")
            print("")
        to_update = int(input("Enter Report ID to update: "))
        for report in reports:
            if report["report_id"] == to_update:
                report_id = report["report_id"]
                print(f'Current Status: {report["current_status"]}')
                break
        status_set = ("On Progress", "For Review", "Completed", "Rejected", "Needs Revision")
        print("\nAllowed New Status: On Progress, For Review, Completed, Rejected, Needs Revision\n")
        new_status = input("Enter new status: ")
        if new_status in status_set:
            for report in reports:
                if report["report_id"] == report_id:
                    current_status = report["current_status"]
                    status_count[current_status] -= 1
                    status_count[new_status] += 1
                    report["status"] = new_status
                    print("Status Updated Successfully.")
                    print(f"New Status: {new_status}")
                    break
    elif option == 4:
        for count in status_count:
            print(f"{count}: {status_count[count]}")
    elif option == 5:
        pass
    else:
        print("\nPlease enter a valid input [1 - 5]\n")