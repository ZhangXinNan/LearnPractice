package com.example.lightsensortest;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import java.util.List;

public class MainActivity extends AppCompatActivity {

    private SensorManager sensorManager;
    private TextView lightLevel;
    private TextView textAcc;
    private TextView textGyr;
    private TextView textMag;
    private TextView textCompass;
    private TextView textSensorsInfo;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        this.lightLevel = (TextView)findViewById(R.id.light_level);
        this.textAcc = findViewById(R.id.acc);
        this.textGyr = findViewById(R.id.gyr);
        this.textMag = findViewById(R.id.mag);
        this.textCompass = findViewById(R.id.compass);
        this.textSensorsInfo = findViewById(R.id.sensors_info);
        // 1. 获取SensorManager实例
        this.sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        // 2.  得到传感器类型
        Sensor sensor = sensorManager.getDefaultSensor(Sensor.TYPE_LIGHT);
        Sensor sensorAccelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        Sensor sensor_gyr = sensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE);
        Sensor sensorMagnetic = sensorManager.getDefaultSensor(Sensor.TYPE_MAGNETIC_FIELD);
        // 4. 注册SensorEventListener使其生效。
        this.sensorManager.registerListener(listener, sensor, SensorManager.SENSOR_DELAY_NORMAL);
        this.sensorManager.registerListener(listener, sensorAccelerometer, SensorManager.SENSOR_DELAY_GAME);
        this.sensorManager.registerListener(listener, sensor_gyr, SensorManager.SENSOR_DELAY_GAME);
        this.sensorManager.registerListener(listener, sensorMagnetic, SensorManager.SENSOR_DELAY_GAME);


//        this.textSensorsInfo.setText(this.getSensorList());
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // 5. 将使用的资源释放掉。
        if (this.sensorManager != null) {
            this.sensorManager.unregisterListener(listener);
        }
    }
    // 3. 对传感器输出的信号进行监听。
    private SensorEventListener listener = new SensorEventListener() {
        float[] accelerometerValues = new float[3];
        float[] magneticValues = new float[3];

        @Override
        public void onSensorChanged(SensorEvent event) {
            String s = new String("");
            for (int i=0; i < event.values.length; i++) {
                s += " " + event.values[i];
            }

            switch (event.sensor.getType()) {
                case Sensor.TYPE_LIGHT:
                    lightLevel.setText("Current light level is " + event.values[0] + " lx");
                    break;
                case Sensor.TYPE_ACCELEROMETER:
                    accelerometerValues = event.values.clone();
                    textAcc.setText("acc : " + s);
                    break;
                case Sensor.TYPE_MAGNETIC_FIELD:
                    magneticValues = event.values.clone();
                    textMag.setText("mag : " + s);
                    break;
                case Sensor.TYPE_GYROSCOPE:
                    textGyr.setText("gyr : " + s);
                    break;
                default:
                    break;
            }
            float[] R = new float[9];
            float[] values = new float[3];
            SensorManager.getRotationMatrix(R, null, accelerometerValues, magneticValues);
            sensorManager.getOrientation(R, values);
            textCompass.setText("compass : " + values[0]);
            Log.d("MainActivity", "values[0] is " + Math.toDegrees(values[0]) );
        }

        @Override
        public void onAccuracyChanged(Sensor sensor, int accuracy) {
        }
    };



    private String getSensorList() {
        // 获取传感器管理器
        SensorManager sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);

        // 获取全部传感器列表
        List<Sensor> sensors = sensorManager.getSensorList(Sensor.TYPE_ALL);

        // 打印每个传感器信息
        StringBuilder strLog = new StringBuilder();
        int iIndex = 1;
        for (Sensor item : sensors) {
            strLog.append(iIndex + ".");
            strLog.append("	Sensor Type - " + item.getType() + "\r\n");
            strLog.append("	Sensor Name - " + item.getName() + "\r\n");
            strLog.append("	Sensor Version - " + item.getVersion() + "\r\n");
            strLog.append("	Sensor Vendor - " + item.getVendor() + "\r\n");
            strLog.append("	Maximum Range - " + item.getMaximumRange() + "\r\n");
            strLog.append("	Minimum Delay - " + item.getMinDelay() + "\r\n");
            strLog.append("	Power - " + item.getPower() + "\r\n");
            strLog.append("	Resolution - " + item.getResolution() + "\r\n");
            strLog.append("\r\n");
            iIndex++;
        }
        return strLog.toString();
    }
}
