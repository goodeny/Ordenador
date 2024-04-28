using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ordenador
{
    internal class CountingSort : IStrategy
    {
        public void Execute(int[] array)
        {
            CountingSortFunction(array);
            /*foreach (int i in CountingSortFunction(array))
            {
                Console.WriteLine(i);
            }*/
        }
        public int[] CountingSortFunction(int[] array)
        {
            var size = array.Length;
            var maxElement = GetMaxVal(array, size);
            var occurrences = new int[maxElement + 1];
            for (int i = 0; i < maxElement + 1; i++)
            {
                occurrences[i] = 0;
            }
            for (int i = 0; i < size; i++)
            {
                occurrences[array[i]]++;
            }
            for (int i = 0, j = 0; i <= maxElement; i++)
            {
                while (occurrences[i] > 0)
                {
                    array[j] = i;
                    j++;
                    occurrences[i]--;
                }
            }
            return array;
        }

        public static int GetMaxVal(int[] array, int size)
        {
            var maxVal = array[0];
            for (int i = 1; i < size; i++)
                if (array[i] > maxVal)
                    maxVal = array[i];
            return maxVal;
        }
    }
}
