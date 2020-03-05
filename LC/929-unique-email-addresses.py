class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:

            email_fields = email.split("@")

            if len(email_fields) != 2:
                raise "Invalid email"

            name = email_fields[0]
            name = name.replace(".", "")
            name = name.split("+")[0]

            unique_emails.add("{}@{}".format(name, email_fields[1]))


        print(unique_emails)
        return len(unique_emails)