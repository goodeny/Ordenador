using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ordenador
{
    internal class QuickSort : IStrategy
    {
        public void Execute(int[] array)
        {

            //QuickSortFunction(array, 0, array.Length - 1);
            foreach (int i in QuickSortFunction(array, 0, array.Length - 1))
            {
                Console.WriteLine(i);
            }
        }

        public int[] QuickSortFunction(int[] array, int leftIndex, int rightIndex)
        {
            var i = leftIndex;
            var j = rightIndex;
            var pivot = array[leftIndex];
            while (i <= j)
            {
                while (array[i] < pivot)
                {
                    i++;
                }

                while (array[j] > pivot)
                {
                    j--;
                }
                if (i <= j)
                {
                    int temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                    i++;
                    j--;
                }
            }

            if (leftIndex < j)
                QuickSortFunction(array, leftIndex, j);
            if (i < rightIndex)
                QuickSortFunction(array, i, rightIndex);
            return array;
        }
    }
}
