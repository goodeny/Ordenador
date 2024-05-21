using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Ordenador
{
    internal class Repository
    {
        public MySql.Data.MySqlClient.MySqlConnection DatabaseExec()
        {
            MySql.Data.MySqlClient.MySqlConnection conn;
            string myConnectionString;
            myConnectionString = "server=localhost;uid=root;" + "pwd=;database=Ordenador";

            conn = new MySql.Data.MySqlClient.MySqlConnection();
            conn.ConnectionString = myConnectionString;
            conn.Open();

            return conn;
        }
        public MySqlDataReader Connect(string query)
        {
            MySqlCommand cmd = new MySqlCommand(query, DatabaseExec());
            MySqlDataReader reader = cmd.ExecuteReader();
            return reader;
        }
        public MySqlDataReader ToSelect(string query)
        {
            MySqlCommand cmd = new MySqlCommand(query, DatabaseExec());
            return cmd.ExecuteReader();
        }
        public void Insert(int size, string time)
        {
            try
            {
                string query = $"insert into Data (size, time) values ({size}, '{time}')";
                Connect(query).Close();
            } catch (MySql.Data.MySqlClient.MySqlException ex)
            {
                Console.WriteLine(ex.Message);
            }           
        }

        public void InsertData2(string name, int size, string time)
        {
            try
            {
                string query = $"insert into Data2 (name, size, time) values ('{name}', {size}, '{time}')";
                Connect(query).Close();
            }
            catch (MySql.Data.MySqlClient.MySqlException ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
