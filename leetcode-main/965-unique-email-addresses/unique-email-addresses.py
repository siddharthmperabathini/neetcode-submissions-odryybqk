class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashset = set()
        for email in emails:
            text = email.split('@')
            local = text[0]
            domain = text[1]
            text = local.split('+')
            hashset.add(text[0].replace('.','') + '@' + domain)
        return len(hashset)
