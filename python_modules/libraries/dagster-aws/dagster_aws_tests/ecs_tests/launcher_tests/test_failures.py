def test_run_task_failure(ecs, instance, workspace, run):
    def run_task(self=ecs, **kwargs):
        self.stubber.activate()
        self.stubber.add_response(
            method="run_task",
            service_response={"tasks": []},
            expected_params={**kwargs},
        )
        response = self.client.run_task(**kwargs)
        self.stubber.deactivate()
        return response

    instance.run_launcher.ecs.run_task = run_task

    instance.launch_run(run.run_id, workspace)
