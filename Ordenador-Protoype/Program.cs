using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Runtime.Remoting.Contexts;
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
            GenerateArray generateArray = new GenerateArray();

            int[] sizes = { 256, 512, 1024, 2048, 5096 };
            
            foreach (int sizex in sizes)
            {
                stopWatch.Start();

                
                int[] array = generateArray.CreateArray(sizex);

                var context = new Context(new CountingSort());
                context.ExecuteStrategy(array);

                var contextClone = (Context)context.Clone();
                contextClone.SetStrategy(new InsertionSort());
                contextClone.ExecuteStrategy(array);

                var contextClone2 = (Context)context.Clone();
                contextClone2.SetStrategy(new QuickSort());
                contextClone2.ExecuteStrategy(array);

                var contextClone3 = (Context)context.Clone();
                contextClone3.SetStrategy(new MargeSort());
                contextClone3.ExecuteStrategy(array);

                var contextClone4 = (Context)context.Clone();
                contextClone4.SetStrategy(new ShellSort());
                contextClone4.ExecuteStrategy(array);

                stopWatch.Stop();
                TimeSpan tsTotal = stopWatch.Elapsed;
                string elapsedTimeTotal = String.Format("{0:00}:{1:00}:{2:00}:{3:00}", tsTotal.Hours, tsTotal.Minutes, tsTotal.Seconds, tsTotal.Milliseconds/ 10);
                Singleton.Instance.ShowElapsedTime(elapsedTimeTotal);
                repository.Insert(sizex, elapsedTimeTotal);
            }

            foreach (int sizex in sizes)
            {
                Stopwatch stopWatch0 = new Stopwatch();
                int[] array = generateArray.CreateArray(sizex);
                stopWatch0.Start();
                var context = new Context(new CountingSort());
                context.ExecuteStrategy(array);
                stopWatch0.Stop();
                TimeSpan ts = stopWatch0.Elapsed;
                string elapsedTime = String.Format("{1:00}:{2:00}:{3:00}", ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds);
                Singleton.Instance.ShowElapsedTime(elapsedTime);
                repository.InsertData2("Counting Sort", sizex, elapsedTime);

            }

            foreach (int sizex in sizes)
            {
                Stopwatch stopWatch1 = new Stopwatch();
                int[] array = generateArray.CreateArray(sizex);
                stopWatch1.Start();
                var context = new Context(new InsertionSort());
                context.ExecuteStrategy(array);
                stopWatch1.Stop();
                TimeSpan ts = stopWatch1.Elapsed;
                string elapsedTime = String.Format("{1:00}:{2:00}:{3:00}", ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds);
                Singleton.Instance.ShowElapsedTime(elapsedTime);
                repository.InsertData2("Insertion Sort", sizex, elapsedTime);

            }

            foreach (int sizex in sizes)
            {
                Stopwatch stopWatch2 = new Stopwatch();
                int[] array = generateArray.CreateArray(sizex);
                stopWatch2.Start();
                var context = new Context(new QuickSort());
                context.ExecuteStrategy(array);
                stopWatch2.Stop();
                TimeSpan ts = stopWatch2.Elapsed;
                string elapsedTime = String.Format("{1:00}:{2:00}:{3:00}", ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds);
                Singleton.Instance.ShowElapsedTime(elapsedTime);
                repository.InsertData2("Quick Sort", sizex, elapsedTime);

            }

            foreach (int sizex in sizes)
            {
                Stopwatch stopWatch3 = new Stopwatch();
                int[] array = generateArray.CreateArray(sizex);
                stopWatch3.Start();
                var context = new Context(new MargeSort());
                context.ExecuteStrategy(array);
                stopWatch3.Stop();
                TimeSpan ts = stopWatch3.Elapsed;
                string elapsedTime = String.Format("{1:00}:{2:00}:{3:00}", ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds);
                Singleton.Instance.ShowElapsedTime(elapsedTime);
                repository.InsertData2("Marge Sort", sizex, elapsedTime);

            }
            foreach (int sizex in sizes)
            {
                Stopwatch stopWatch4 = new Stopwatch();
                int[] array = generateArray.CreateArray(sizex);
                stopWatch4.Start();
                var context = new Context(new ShellSort());
                context.ExecuteStrategy(array);
                stopWatch4.Stop();
                TimeSpan ts = stopWatch4.Elapsed;
                string elapsedTime = String.Format("{1:00}:{2:00}:{3:00}", ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds);
                Singleton.Instance.ShowElapsedTime(elapsedTime);
                repository.InsertData2("Shell Sort", sizex, elapsedTime);

            }

            Console.ReadKey();
        }
    }
}
