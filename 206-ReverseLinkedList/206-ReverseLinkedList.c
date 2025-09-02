// Last updated: 9/2/2025, 1:42:34 PM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 typedef struct ListNode node;
struct ListNode* reverseList(struct ListNode* head) {
    node *pn=NULL;
    node *cn=head;
    node *nn=head;
    while(cn!=NULL){
        nn=nn->next;
        cn->next=pn;
        pn=cn;
        cn=nn;  
    }
    return pn;
    
}