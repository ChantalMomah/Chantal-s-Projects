#include <iostream>
#include <string>
using namespace std;

class Invoice {
private:
    string partNumber;
    string partDescription;
    int quantity;
    int pricePerItem;

public:
    Invoice(string partNumber, string partDescription, int quantity, int pricePerItem) {
        setPartNumber(partNumber);
        setPartDescription(partDescription);
        setQuantity(quantity);
        setPricePerItem(pricePerItem);
    }

    void setPartNumber(string partNumber) {
        this->partNumber = partNumber;
    }

    void setPartDescription(string partDescription) {
        this->partDescription = partDescription;
    }

    void setQuantity(int quantity) {
        this->quantity = (quantity > 0) ? quantity : 0;
    }

    void setPricePerItem(int pricePerItem) {
        this->pricePerItem = (pricePerItem > 0) ? pricePerItem : 0;
    }

    string getPartNumber() const {
        return partNumber;
    }

    string getPartDescription() const {
        return partDescription;
    }

    int getQuantity() const {
        return quantity;
    }

    int getPricePerItem() const {
        return pricePerItem;
    }

    int getInvoiceAmount() const {
        return quantity * pricePerItem;
    }
};

int main() {
    Invoice invoice("A123", "Hammer", 10, 25);

    cout << "Part Number: " << invoice.getPartNumber() << endl;
    cout << "Part Description: " << invoice.getPartDescription() << endl;
    cout << "Quantity: " << invoice.getQuantity() << endl;
    cout << "Price Per Item: " << invoice.getPricePerItem() << endl;
    cout << "Invoice Amount: " << invoice.getInvoiceAmount() << endl;

    invoice.setQuantity(-5);
    invoice.setPricePerItem(-10);

    cout << "\nAfter setting invalid values:" << endl;
    cout << "Quantity: " << invoice.getQuantity() << endl;
    cout << "Price Per Item: " << invoice.getPricePerItem() << endl;
    cout << "Invoice Amount: " << invoice.getInvoiceAmount() << endl;

    return 0;
}
