using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Mysqlx.Crud;

namespace Ordenador
{
    public class Context : ICloneable
    {
        private SortAbstraction _sortAbstraction;

        public Context(SortAbstraction sortAbstraction)
        {
            _sortAbstraction = sortAbstraction;
        }

        public void SetSortAbstraction(SortAbstraction sortAbstraction)
        {
            _sortAbstraction = sortAbstraction;
        }

        public void ExecuteStrategy(int[] array)
        {
            _sortAbstraction.Sort(array);
        }

        public object Clone()
        {
            return new Context(_sortAbstraction);
        }
    }

}
