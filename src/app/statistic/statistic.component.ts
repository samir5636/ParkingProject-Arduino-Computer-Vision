import {Component, numberAttribute, OnInit} from '@angular/core';
import { Chart } from 'angular-highcharts';
import {CarServiceService} from "../services/car-service.service";
import {NumbrCarTotal} from "../modules/NmbrCarTotalAndInParking";
import {NumberCarIN} from "../modules/Total";

@Component({
  selector: 'app-statistic',
  templateUrl: './statistic.component.html',
  styleUrls: ['./statistic.component.css']
})
export class StatisticComponent implements OnInit {
  // lineChart!: Chart;
  pieChart!: Chart;
  nbrT!:NumbrCarTotal;
  inP!:NumberCarIN;

  constructor(private carsirvice : CarServiceService) {
  }

  ngOnInit(): void {
    this.handelNbrTotal();
    this.handelNbrCarInParking();
  }

  private createPieChart(): void {
    console.log('Data:', this.nbrT,"333", this.inP);

      console.log('Creating pie chart...');

      const totalCars = this.nbrT.number;
      const carsInParking = this.inP.number;

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
            name: 'Cars',
            data: [
              { name: 'Cars out Parking', y: totalCars, color: '#02a3b9' },
              { name: 'Cars in Parking', y: carsInParking, color: '#000000' },
            ]
          } as any
        ]
      });

      console.log('Pie chart created:', this.pieChart);

  }

  handelNbrTotal(): void {
    this.carsirvice.nbrTotalCar().subscribe({
      next: (data :NumbrCarTotal) => {
        console.log('NbrTotalCar data:', data);
        this.nbrT = data;
        this.createPieChart();
      },
      error: (error) => {
        console.error('NbrTotalCar error:', error);
      },
    });
  }

  handelNbrCarInParking(): void {
    this.carsirvice.nbrCarInparking().subscribe({
      next: (data:NumberCarIN) => {
        console.log('NbrCarInparking data:', data);
        this.inP = data;
        this.createPieChart();
      },
      error: (error) => {
        console.error('NbrCarInparking error:', error);
      },
    });
  }

}
