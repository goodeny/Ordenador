using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Mysqlx.Crud;

namespace Ordenador
{
    public abstract class SortAbstraction
    {
        protected ISortImplementation _sortImplementation;

        public SortAbstraction(ISortImplementation sortImplementation)
        {
            _sortImplementation = sortImplementation;
        }

        public void SetSortImplementation(ISortImplementation sortImplementation)
        {
            _sortImplementation = sortImplementation;
        }

        public abstract void Sort(int[] array);
    }
}
