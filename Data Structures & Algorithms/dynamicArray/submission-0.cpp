class DynamicArray {
private:
    int capacity;
    int size;
    int* arr;
public:

    DynamicArray(int capacity) {
        this->capacity = capacity;
        this->size = 0;
        this->arr = new int[capacity];
    }

    int get(int i) {
        return this->arr[i];
    }

    void set(int i, int n) {
        this->arr[i] = n;
    }

    void pushback(int n) {
        if (this->size == this->capacity) {
            this->resize();
        }
        arr[size] = n;
        size++;
    }

    int popback() {
        this->size--;
        return this->arr[size];
    }

    void resize() {
        this->capacity *= 2;
        int* new_arr = new int[capacity];
        for (int i = 0; i < size; ++i) {
            new_arr[i] = arr[i];
        }
        delete[] arr;
        this->arr = new_arr;
    }

    int getSize() {
        return this->size;
    }

    int getCapacity() {
        return this->capacity;
    }
};
