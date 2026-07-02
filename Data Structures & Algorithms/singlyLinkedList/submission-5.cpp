class LinkedList {
private:
    class Node {
    public:
        int val;
        Node* next;

        Node(int val) {
            this->val = val;
            this->next = nullptr;
        }
    };

    Node* head;

public:
    LinkedList() {
        head = nullptr;
    }

    int get(int index) {
        Node* curr = head;

        for (int i = 0; i < index; ++i) {
            if (!curr) {
                return -1;
            }
            curr = curr->next;
        }
        if (!curr) {
            return -1;
        }
        return curr->val;
    }

    void insertHead(int val) {
        Node* node = new Node(val);
        node->next = head;
        head = node;
    }
    
    void insertTail(int val) {
        if (!head) {
            insertHead(val);
            return;
        }

        Node* curr = head;
        while (curr->next) {
            curr = curr->next;
        }
        Node* node = new Node(val);
        curr->next = node;
    }

    bool remove(int index) {
        Node* curr = head;
        Node* prev = nullptr;

        for (int i = 0; i < index; ++i) {
            if (!curr) {
                return false;
            }
            prev = curr;
            curr = curr->next;
        }
        if (!curr) {
            return false;
        }

        if (index == 0) {
            head = curr->next;
            delete curr;
            return true;
        }

        prev->next = curr->next;
        delete curr;
        return true;
    }

    vector<int> getValues() {
        vector<int> vals;
        Node* curr = head;
        while (curr) {
            vals.push_back(curr->val);
            curr = curr->next;
        }
        return vals;
    }
};
