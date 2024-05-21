using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Mysqlx.Crud;

namespace Ordenador
{
    public class SortClient : SortAbstraction
    {
        public SortClient(ISortImplementation sortImplementation) : base(sortImplementation) { }

        public override void Sort(int[] array)
        {
            _sortImplementation.Sort(array);
        }
    }

}
