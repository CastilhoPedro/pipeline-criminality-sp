from utils.support import *
from utils.folders import *
import pandas as pd
import os
import userpaths as usr



class formatacaoDados:
    def __init__(self):
        
        self.dfcolumns=[
            'Homicídio Doloso',
            'Nº De Vítimas Em Homicídio Doloso',
            'Homicídio Doloso Por Acidente De Trânsito',
            'Nº De Vítimas Em Homicídio Doloso Por Acidente De Trânsito',
            'Homicídio Culposo Por Acidente De Trânsito',
            'Homicídio Culposo Outros',
            'Tentativa De Homicídio',
            'Lesão Corporal Seguida De Morte',
            'Lesão Corporal Dolosa',
            'Lesão Corporal Culposa Por Acidente De Trânsito',
            'Lesão Corporal Culposa - Outras',
            'Latrocínio',
            'Nº De Vítimas Em Latrocínio',
            'Total De Estupro',
            'Estupro',
            'Estupro De Vulnerável',
            'Total De Roubo - Outros',
            'Roubo - Outros',
            'Roubo De Veículo',
            'Roubo A Banco',
            'Roubo De Carga',
            'Furto - Outros',
            'Furto De Veículo',
            'Mes',
            'Ano',
            'Municipio'
        ]
        
        self.main_folder = landzonepath
        self.main_df = pd.DataFrame(columns=self.dfcolumns)

        

    def __get_years(self, file_path: str) -> list[str]:
        """Reads the SSP portal Excel file and returns it's years list (each year is a sheetname).

        Args:
            file_path (str): portal file path

        Returns:
            list: years list. Example: [2025, 2024, 2023]
        """
        df = pd.read_excel(file_path, sheet_name=None)
        return list(df.keys())

    def insert_date_columns(self, df: pd.DataFrame, year: str) -> pd.DataFrame:
        """Adds month and year columns to a DataFrame based on its index values.

        Args:
            df (pd.DataFrame): Input DataFrame.
            year (str/int): Year to be added to all rows. Example: 2023 or "2023"

        Returns:
            pd.DataFrame: Same DataFrame with two filled columns:
                - 'Mes': Month numbers from the index (e.g., 1 for January)
                - 'Ano': Year repeated for all rows

        Example:
            >>> df = pd.DataFrame({'Crimes': [100, 200]}, index=[1, 2])  # Index = month numbers
            >>> df = insert_date_columns(df, 2023)
            >>> print(df)
            Crimes  Mes   Ano
            1    100    1  2023
            2    200    2  2023

        """
        df['Mes'] = df.index
        df['Ano'] = year
        return df

    def insert_city(self, file_path: str, df: pd.DataFrame) -> pd.DataFrame:
        """Adds city name column to a DataFrame based on file name.

        Args:
            file_path (str): DataFrame file path. Will be used to get city name.
            df (pd.DataFrame): Input DataFrame.

        Raises:
            ValueError: In case of none of three cities (Barueri, Cajamar, Santana de Parnaíba) were found in file name.

        Returns:
            pd.DataFrame: Same DataFrame with a filled column:
                - 'Municipio': City repeated for all rows.
        
        Example:
            >>> df = pd.DataFrame({'Crimes': [100, 200]})
            >>> df = insert_city(df, 'C:\\Users\\Documents\\temp\\landing zone\\OcorrenciaMensal(Criminal)-Barueri_20250630_202627.xlsx')
            >>> print(df)
            Crimes  Municipio
            1    100    Barueri
            2    200    Barueri
        """

        for i in list_cities:
            if i in file_path:
                df['Municipio'] = i
                return df
        raise ValueError(f"City not found in list {list_cities}, please check the excel file {file_path.split('//')[-1]}")

    def clear_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Remove missing values, wrong values (e.g. string values in int Series).

        Args:
            df (pd.DataFrame): Input DataFrame.

        Returns:
            pd.DataFrame: Same DataFrame with a new column (Total).
                
        """
        df = df.loc[(df['Mes'] != 'Total') & (df['Homicídio Doloso'] != '...')]
        return df

    def add_total_column(self, df: pd.DataFrame) -> pd.DataFrame:
        """Set each Series type between int and str and adds the total column, which is the sum of a specific crime over the months

        Args:
            df (pd.DataFrame): Input DataFrame.

        Returns:
            pd.DataFrame: Same DataFrame with a new column (Total).
                
        """
        int_columns = ['Homicídio Doloso', 'Nº De Vítimas Em Homicídio Doloso',
        'Homicídio Doloso Por Acidente De Trânsito',
        'Nº De Vítimas Em Homicídio Doloso Por Acidente De Trânsito',
        'Homicídio Culposo Por Acidente De Trânsito',
        'Homicídio Culposo Outros', 'Tentativa De Homicídio',
        'Lesão Corporal Seguida De Morte', 'Lesão Corporal Dolosa',
        'Lesão Corporal Culposa Por Acidente De Trânsito',
        'Lesão Corporal Culposa - Outras', 'Latrocínio',
        'Nº De Vítimas Em Latrocínio', 'Total De Estupro', 'Estupro',
        'Estupro De Vulnerável', 'Total De Roubo - Outros', 'Roubo - Outros',
        'Roubo De Veículo', 'Roubo A Banco', 'Roubo De Carga', 'Furto - Outros',
        'Furto De Veículo']

        str_columns = ['Ano', 'Mes', 'Municipio']

        df[int_columns] = df[int_columns].astype(int)
        df[str_columns] = df[str_columns].astype(str)

        subdf = df[int_columns]
        df['Total'] = subdf.sum(axis=1)
        return df

    def process_data(self, file_path: str) -> pd.DataFrame:
        
        for year in self.__get_years(file_path):
            
            df = pd.read_excel(file_path, sheet_name=year)
            df = df.transpose()
            
            self.insert_date_columns(df=df, year=year)

            if len(df.columns) == 25:
                df.columns = self.dfcolumns[:-1]
            elif len(df.columns) == 26:
                df.columns = self.dfcolumns
            
            
            df = df.drop(df.index[0])
            
            df = self.insert_city(file_path, df)
            df = self.clear_data(df)
            df = self.add_total_column(df)

            self.main_df = pd.concat([self.main_df, df])
        return self.main_df


