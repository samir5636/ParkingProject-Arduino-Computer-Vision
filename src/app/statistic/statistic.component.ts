import { Component, OnInit } from '@angular/core';
import { Chart } from 'angular-highcharts';

@Component({
  selector: 'app-statistic',
  templateUrl: './statistic.component.html',
  styleUrls: ['./statistic.component.css']
})
export class StatisticComponent implements OnInit {
  lineChart!: Chart;
  pieChart!: Chart;

  ngOnInit(): void {
    // Générez des données pour le graphique en ligne (croissance linéaire)
    const lineChartData = this.generateLineChartData();

    // Créez le graphique en ligne
    this.lineChart = new Chart({
      chart: {
        type: 'line'
      },
      title: {
        text: 'Parking Development'
      },
      credits: {
        enabled: false
      },
      series: [
        {
          name: 'Cars in parking',
          data: lineChartData
        } as any
      ]
    });

    // Créez le graphique en secteur
    this.pieChart = new Chart({
      chart: {
        type: 'pie',
        plotShadow: false,
      },
      credits: {
        enabled: false
      },
      plotOptions: {
        pie: {
          innerSize: '99%',
          borderWidth: 10,
          borderColor: '',
          slicedOffset: 10,
          dataLabels: {
            connectorWidth: 0,
          },
        }
      },
      title: {
        verticalAlign: 'middle',
        floating: true,
        text: 'Parking',
      },
      legend: {
        enabled: false,
      },
      series: [
        {
          type: 'pie',
          name: 'Cars in parking',
          data: [
            { name: 'Cars In Parking', y: lineChartData[lineChartData.length - 1], color: '#02a3b9' },
            { name: 'Cars out Parking', y: 20000, color: '#000000' },
          ]
        } as any
      ]
    });
  }

  // Fonction pour générer des données de croissance linéaire
  generateLineChartData(): number[] {
    const data = [];
    for (let i = 1; i <= 10; i++) {
      // Utilisez une fonction mathématique simple pour simuler la croissance
      const carsInParking = 1000 * i;
      data.push(carsInParking);
    }
    return data;
  }
}
