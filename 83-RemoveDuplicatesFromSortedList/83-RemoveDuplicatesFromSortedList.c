// Last updated: 9/2/2025, 1:43:27 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    
    if(head!=NULL)
    {
    struct ListNode* prev=head;
    struct ListNode* curr=head->next;
    struct ListNode* temp=NULL;
    while(curr!=NULL&& head!=NULL)
    {
        if(prev->val==curr->val)
        {
            temp=curr;
            prev->next=curr->next;
            curr=curr->next;
        }
        else{
            prev=prev->next;
            curr=curr->next;
        }

    }
    return head;
    
    }
    return head;
    
}