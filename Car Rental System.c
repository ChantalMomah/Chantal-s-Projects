#include <iostream>
using namespace std;

const int daily_charge = 30000;
const int kilo_charge = 1200;
const int ratePerLiter = 1030;

double calculateDailyCharge(int numOfDays, double dailyRate);
double calculateKilometerCharge(int kilometers, double ratePerKilometer);
double calculateFuelPrice(double numOfLiters, double ratePerLiter);
int getKilometersDriven();
double calculateTotalRent(int numOfDays, int kilometersDriven, double fuelConsumption);

int main() {
    int numOfDays;
    int startOdometer, endOdometer;
    double fuelConsumption;

    cout << "Enter the number of rental days: ";
    cin >> numOfDays;

    cout << "Enter the start odometer reading in km: ";
    cin >> startOdometer;
    cout << "Enter the end odometer reading in km: ";
    cin >> endOdometer;

    cout << "Enter the amount of fuel consumed in liters: ";
    cin >> fuelConsumption;

    int kilometersDriven = endOdometer - startOdometer;
    if (kilometersDriven < 0) {
        cout << "There's an error. Please check the inputed values";
        return kilometersDriven;
    }

    double totalRent = calculateTotalRent(numOfDays, kilometersDriven, fuelConsumption);

    cout << "Car Rental Details";
    cout << "Daily Charge: " << calculateDailyCharge(numOfDays, daily_charge) << endl;
    cout << "Kilometer Charge: " << calculateKilometerCharge(kilometersDriven, kilo_charge) << endl;
    cout << "Fuel Charge: " << calculateFuelPrice(fuelConsumption, ratePerLiter) << endl;
    cout << "Total Rent: " << totalRent << endl;

    return 0;
}

double calculateDailyCharge(int numOfDays, double dailyRate) {
    return numOfDays * dailyRate;
}

double calculateKilometerCharge(int kilometers, double ratePerKilometer) {
    return kilometers * ratePerKilometer;
}

double calculateFuelPrice(double numOfLiters, double ratePerLiter) {
    return numOfLiters * ratePerLiter;
}

double calculateTotalRent(int numOfDays, int kilometersDriven, double fuelConsumption) {
    double dailyCharge = calculateDailyCharge(numOfDays, daily_charge);
    double kilometerCharge = calculateKilometerCharge(kilometersDriven, kilo_charge);
    double fuelCharge = calculateFuelPrice(fuelConsumption, ratePerLiter);
    return dailyCharge + kilometerCharge + fuelCharge;
}
