public class LinkedList {

    public ListNode removeNth (ListNode head , int n){
        ListNode left = head ;
        ListNode right = head ;

        if(head.next == null){
            return null;
        }
        int count = n;
        while(n>0 && right != null){
            right = right.next;
            n-=1;
        }

        while (right != null) {
            right=right.next;
            if(right != null){
                left=left.next;
            }
        }
        if(left == head && count ==2){
            head.next = null;
        }
        left.next = left.next.next;

        return head;


    }
}

