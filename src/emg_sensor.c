#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/adc.h"
#include "esp_adc_cal.h"

#define SENSOR_PIN ADC1_CHANNEL_0  // GPIO36 is ADC1_CHANNEL_0

void app_main(void)
{
    // Initialize serial communication
    printf("MyoWare Example_01_analogRead_SINGLE (ESP32 - ESP-IDF)\n");

    // ADC Configuration
    adc1_config_width(ADC_WIDTH_BIT_12); // 12-bit ADC resolution
    adc1_config_channel_atten(SENSOR_PIN, ADC_ATTEN_DB_11); // 11dB attenuation for full voltage range (0-3.3V)

    while (1)
    {
        int sensorValue = adc1_get_raw(SENSOR_PIN); // Read the analog value from GPIO36
        printf("%d\n", sensorValue); // Print only the raw sensor value

        vTaskDelay(pdMS_TO_TICKS(50)); // 50ms delay
    }
}
