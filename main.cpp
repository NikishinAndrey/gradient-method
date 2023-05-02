#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

double f(vector<double> x) {
    return 2 * x[0] * x[0] + 3 * x[1] * x[1] - 4 * x[0] * x[1] + 5 * x[0] - 6 * x[1] + 7;
}

vector<double> gradient_f(vector<double> x) {
    vector<double> grad;
    grad.push_back(4 * x[0] - 4 * x[1] + 5);
    grad.push_back(6 * x[1] - 4 * x[0] - 6);
    return grad;
}

vector<vector<double>> gradient_descent(vector<double> x_0, double alpha, int num_iterations) {
    vector<double> x = x_0;
    vector<vector<double>> massive_x(num_iterations, std::vector<double>(2));
    for (int i = 0; i < num_iterations; i++) {
        vector<double> grad = gradient_f(x);
        for (int j = 0; j < x.size(); j++) {
            x[j] = x[j] - alpha * grad[j];
            massive_x[i][j] = x[j];
        }
    }
    return massive_x;
}

int main() {
    vector<double> x0 = {8, 8}; // initial point
    double alpha = 0.15; // velocity train
    int num_iterations = 100; // numbers iteration
    vector<vector<double>> result = gradient_descent(x0, alpha, num_iterations);

    ofstream fout("result.txt");
    if (fout.is_open()) {
        for (int j = 0; j < num_iterations; j++) {
            fout << result[j][0] << ',';
            fout << result[j][1] << ',';
            fout << f(result[j]) << ',';
            fout << endl;
        }
        fout.close();
    }

    return 0;
}
