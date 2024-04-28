using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ordenador
{
    internal class InsertionSort : IStrategy
    {
        public void Execute(int[] array)
        {
            SortArray(array, array.Length);
            /*foreach (int i in SortArray(array, array.Length))
            {
                Console.WriteLine(i);
            }*/
        }
        public int[] SortArray(int[] array, int length)
        {
            for (int i = 1; i < length; i++)
            {
                var key = array[i];
                var flag = 0;
                for (int j = i - 1; j >= 0 && flag != 1;)
                {
                    if (key < array[j])
                    {
                        array[j + 1] = array[j];
                        j--;
                        array[j + 1] = key;
                    }
                    else flag = 1;
                }
            }
            return array;
        }
    }
}
