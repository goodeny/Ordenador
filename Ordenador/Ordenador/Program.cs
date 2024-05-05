using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Security.Policy;
using System.Text;
using System.Threading.Tasks;

namespace Ordenador
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Repository repository = new Repository();
            Stopwatch stopWatch = new Stopwatch();   
            Program program = new Program();
      
            int[] sizes = { 256, 512, 1024, 2048, 5096 };
            
            foreach (int sizex in sizes)
            {
                stopWatch.Start();
                program.ExecuteCountingSort(sizex);  
                program.ExecuteInsertionSort(sizex);
                program.ExecuteQuickSort(sizex);
                program.ExecuteMargeSort(sizex);
                program.ExecuteShellSort(sizex); //256
                stopWatch.Stop();
                TimeSpan tsTotal = stopWatch.Elapsed;
                string elapsedTimeTotal = String.Format("{0:00}:{1:00}:{2:00}:{3:00}", tsTotal.Hours, tsTotal.Minutes, tsTotal.Seconds, tsTotal.Milliseconds / 10);
                Singleton.Instance.ShowElapsedTime(elapsedTimeTotal);
                repository.Insert(sizex, elapsedTimeTotal);
            }
            

            foreach (int sizex in sizes)
            {
                stopWatch.Start();
                program.ExecuteCountingSort(sizex);
                stopWatch.Stop();
                TimeSpan ts = stopWatch.Elapsed;
                string elapsedTime = String.Format("{0:00}:{1:00}:{2:00}:{3:00}", ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds / 10);
                Singleton.Instance.ShowElapsedTime(elapsedTime);
                repository.InsertData2("Counting Sort", sizex, elapsedTime);

            }

            foreach (int sizex in sizes)
            {
                stopWatch.Start();
                program.ExecuteInsertionSort(sizex);
                stopWatch.Stop();
                TimeSpan ts = stopWatch.Elapsed;
                string elapsedTime = String.Format("{0:00}:{1:00}:{2:00}:{3:00}", ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds / 10);
                Singleton.Instance.ShowElapsedTime(elapsedTime);
                repository.InsertData2("Insertion Sort", sizex, elapsedTime);

            }

            foreach (int sizex in sizes)
            {
                stopWatch.Start();
                program.ExecuteQuickSort(sizex);
                stopWatch.Stop();
                TimeSpan ts = stopWatch.Elapsed;
                string elapsedTime = String.Format("{0:00}:{1:00}:{2:00}:{3:00}", ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds / 10);
                Singleton.Instance.ShowElapsedTime(elapsedTime);
                repository.InsertData2("Quick Sort", sizex, elapsedTime);

            }

            foreach (int sizex in sizes)
            {
                stopWatch.Start();
                program.ExecuteMargeSort(sizex);
                stopWatch.Stop();
                TimeSpan ts = stopWatch.Elapsed;
                string elapsedTime = String.Format("{0:00}:{1:00}:{2:00}:{3:00}", ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds / 10);
                Singleton.Instance.ShowElapsedTime(elapsedTime);
                repository.InsertData2("Marge Sort", sizex, elapsedTime);

            }
            foreach (int sizex in sizes)
            {
                stopWatch.Start();
                program.ExecuteShellSort(sizex);
                stopWatch.Stop();
                TimeSpan ts = stopWatch.Elapsed;
                string elapsedTime = String.Format("{0:00}:{1:00}:{2:00}:{3:00}", ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds / 10);
                Singleton.Instance.ShowElapsedTime(elapsedTime);
                repository.InsertData2("Shell Sort", sizex, elapsedTime);

            }
            Console.ReadKey();
        }
        public void ExecuteCountingSort(int size)
        {
            GenerateArray generateArray = new GenerateArray();
            CountingSort sort = new CountingSort();
            var context = new Context(sort);
            int[] array = generateArray.CreateArray(size);
            context.ExecuteStrategy(array);
        }
        public void ExecuteInsertionSort(int size)
        {
            GenerateArray generateArray = new GenerateArray();
            InsertionSort insertionSort = new InsertionSort();
            var context = new Context(insertionSort);
            int[] array = generateArray.CreateArray(size);
            context.ExecuteStrategy(array);
        }

        public void ExecuteQuickSort(int size)
        {
            GenerateArray generateArray = new GenerateArray();
            QuickSort quicksort = new QuickSort();
            var context = new Context(quicksort);
            int[] array = generateArray.CreateArray(size);
            context.ExecuteStrategy(array);
        }
        public void ExecuteMargeSort(int size)
        {
            GenerateArray generateArray = new GenerateArray();
            MargeSort margesort = new MargeSort();
            var context = new Context(margesort);
            int[] array = generateArray.CreateArray(size);
            context.ExecuteStrategy(array);
        }
        public void ExecuteShellSort(int size)
        {
            GenerateArray generateArray = new GenerateArray();
            ShellSort shellsort = new ShellSort();
            var context = new Context(shellsort);
            int[] array = generateArray.CreateArray(size);
            context.ExecuteStrategy(array);
        }
    }
}
