using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ordenador
{
    internal class ShellSort : IStrategy
    {
        public void Execute(int[] array)
        {
            ShellSortFunction(array, array.Length, string.Empty);
            /*foreach (int i in ShellSortFunction(array, array.Length, string.Empty))
            {
                Console.WriteLine(i);
            }*/
        }

        public int[] ShellSortFunction(int[] array, int size, string arrayName)
        {
            for (int interval = size / 2; interval > 0; interval /= 2)
            {
                for (int i = interval; i < size; i++)
                {
                    var currentKey = array[i];
                    var k = i;
                    while (k >= interval && array[k - interval] > currentKey)
                    {
                        array[k] = array[k - interval];
                        k -= interval;
                    }
                    array[k] = currentKey;
                }
            }
            return array;
        }
    }
}
