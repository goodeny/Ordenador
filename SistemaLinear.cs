using System;

public interface IMatrixDecomposition
{
    void Decompose(double[,] A, double[] b, out double[,] L, out double[,] U, out double[] x);
}

public class LUDecomposition : IMatrixDecomposition
{
    public void Decompose(double[,] A, double[] b, out double[,] L, out double[,] U, out double[] x)
    {
        int n = A.GetLength(0);
        L = new double[n, n];
        U = new double[n, n];
        x = new double[n];
        double[] y = new double[n];

        // Initialize L to identity matrix and U to zero matrix
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (i == j)
                    L[i, j] = 1;
                else
                    L[i, j] = 0;

                U[i, j] = 0;
            }
        }

        // Decomposition process
        for (int i = 0; i < n; i++)
        {
            for (int j = i; j < n; j++)
            {
                double sum = 0;
                for (int k = 0; k < i; k++)
                    sum += (L[i, k] * U[k, j]);
                U[i, j] = A[i, j] - sum;
            }

            for (int j = i + 1; j < n; j++)
            {
                double sum = 0;
                for (int k = 0; k < i; k++)
                    sum += (L[j, k] * U[k, i]);
                L[j, i] = (A[j, i] - sum) / U[i, i];
            }
        }

        // Forward substitution to solve Ly = b
        for (int i = 0; i < n; i++)
        {
            double sum = 0;
            for (int k = 0; k < i; k++)
                sum += L[i, k] * y[k];
            y[i] = (b[i] - sum);
        }

        // Backward substitution to solve Ux = y
        for (int i = n - 1; i >= 0; i--)
        {
            double sum = 0;
            for (int k = i + 1; k < n; k++)
                sum += U[i, k] * x[k];
            x[i] = (y[i] - sum) / U[i, i];
        }
    }
}

public class MatrixSolver
{
    private IMatrixDecomposition _decompositionStrategy;

    public MatrixSolver(IMatrixDecomposition decompositionStrategy)
    {
        _decompositionStrategy = decompositionStrategy;
    }

    public void SetStrategy(IMatrixDecomposition decompositionStrategy)
    {
        _decompositionStrategy = decompositionStrategy;
    }

    public void Solve(double[,] A, double[] b)
    {
        _decompositionStrategy.Decompose(A, b, out double[,] L, out double[,] U, out double[] x);

        Console.WriteLine("Matrix L:");
        PrintMatrix(L);
        Console.WriteLine("Matrix U:");
        PrintMatrix(U);
        Console.WriteLine("Solution x:");
        PrintVector(x);
    }

    private void PrintMatrix(double[,] matrix)
    {
        for (int i = 0; i < matrix.GetLength(0); i++)
        {
            for (int j = 0; j < matrix.GetLength(1); j++)
            {
                Console.Write(matrix[i, j] + "\t");
            }
            Console.WriteLine();
        }
    }

    private void PrintVector(double[] vector)
    {
        foreach (var value in vector)
        {
            Console.Write(value + "\t");
        }
        Console.WriteLine();
    }
}

public class MatrixGenerator
{
    public static double[,] Generate3x3Matrix()
    {
        Random rand = new Random();
        double[,] matrix = new double[3, 3];
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                matrix[i, j] = rand.NextDouble() * 10;
            }
        }
        return matrix;
    }

    public static double[] Generate3x1Matrix()
    {
        Random rand = new Random();
        double[] matrix = new double[3];
        for (int i = 0; i < 3; i++)
        {
            matrix[i] = rand.NextDouble() * 10;
        }
        return matrix;
    }
}

public class Program
{
    public static void Main(string[] args)
    {
        double[,] A = MatrixGenerator.Generate3x3Matrix();
        double[] b = MatrixGenerator.Generate3x1Matrix();

        Console.WriteLine("Matrix A:");
        PrintMatrix(A);
        Console.WriteLine("Matrix b:");
        PrintVector(b);

        IMatrixDecomposition luDecomposition = new LUDecomposition();
        MatrixSolver solver = new MatrixSolver(luDecomposition);

        solver.Solve(A, b);
    }

    private static void PrintMatrix(double[,] matrix)
    {
        for (int i = 0; i < matrix.GetLength(0); i++)
        {
            for (int j = 0; j < matrix.GetLength(1); j++)
            {
                Console.Write(matrix[i, j] + "\t");
            }
            Console.WriteLine();
        }
    }

    private static void PrintVector(double[] vector)
    {
        foreach (var value in vector)
        {
            Console.Write(value + "\t");
        }
        Console.WriteLine();
    }
}
