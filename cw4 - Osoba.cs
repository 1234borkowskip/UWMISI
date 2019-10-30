using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cw4
{
    class Osoba
    {
        protected string imie;
        protected string nazwisko;
        protected int dataUrodzenia;
        protected string miejsceZamieszkania;

        protected Osoba(string imie, string nazwisko, int dataUrodzenia, string miejsceZamieszkania)
        {
            this.imie = imie;
            this.nazwisko = nazwisko;
            this.dataUrodzenia = dataUrodzenia;
            this.miejsceZamieszkania = miejsceZamieszkania;
        }

        protected void Wypiszinfo()
        {
            Console.WriteLine(imie + " " + nazwisko + " " + dataUrodzenia + " " + miejsceZamieszkania);
        }
    }
}
