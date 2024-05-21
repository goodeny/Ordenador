using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace Ordenador
{
    internal class Generator
    {
        public int b = 0;        
        public List<int> random_numbers(int bytes)
        {
            List<int> emptyList = new List<int>();
            while (size(emptyList) < bytes)
            {
                emptyList.Add(1);
            }
            b = bytes;
            return emptyList;
        }
        public long size<T>(List<T> list)
        {
            int sizeElement = Marshal.SizeOf(typeof(T));
            return (long)list.Capacity * sizeElement;
        }
    }
}
