// Last updated: 9/2/2025, 1:43:04 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    
    if(head==NULL || head->next==NULL)
        return 0;
    struct ListNode *slow=head;
    struct ListNode *fast=head->next;
    while(slow!=fast)
    {
        if(fast==NULL || fast->next==NULL)
        {
            return 0;
        }
        slow=slow->next;
        fast=fast->next->next;
    }
    return 1;
}
    